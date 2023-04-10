from sqlparse.sql import Function, Identifier
import sqlparse
import re


mapped_functions = []


def extract_function_name(function):
    return function.value


def map_instructions(function_body, instructions):
    if function_body.ttype and function_body.ttype[0] == 'Literal':
        for instr in instructions:
            function = mapped_functions[-1]
            function['instructions'][instr] = None
            if re.search(
                    r"\b(EXEC|EXECUTE)\b", function_body.value, re.IGNORECASE):
                function['instructions'][instr] = True if re.search(
                    r"(?<!--\s)\b" + instr + r"\b", function_body.value, re.IGNORECASE) else False
            else:
                function['instructions'][instr] = True if re.search(
                    r"(?<!--\s)(?<!')\b" + instr + r"\b(?!')", function_body.value, re.IGNORECASE) else False


def map_owner(token):
    if re.match(r'^OWNER$', token.value, flags=re.IGNORECASE):
        for i in token.parent.tokens:
            if isinstance(i, Identifier):
                mapped_functions[-1]['owner'] = i.value


def map_function(function):
    if isinstance(function, Function):
        function_name = extract_function_name(function)
        if not mapped_functions or mapped_functions[-1]['name'] != function_name:
            mapped_functions.append(
                {'name': function_name, 'instructions': {}, 'owner': ''})


def map_tokens(tokens, instructions):
    for token in tokens:
        map_function(token)
        map_instructions(token, instructions)
        map_owner(token)


def extract_tokens(parsed_sql, instructions):
    for statement in parsed_sql:
        map_tokens(statement.tokens, instructions)


def map_functions(parsed_sql, instructions):
    extract_tokens(parsed_sql, instructions)
    return mapped_functions
