import sqlparse
from sqlparse.sql import Function, Identifier


def extract_function_info(sql_script):
    parsed = sqlparse.parse(sql_script)
    function_info = []

    for statement in parsed:
        functions = [
            token for token in statement.tokens if isinstance(token, Function)]
        for function in functions:
            # 1. Get function name and parameters
            function_name = function.get_name()
            function_params = [param.strip()
                               for param in function.get_parameters()]

            # 2. Get instructions in the query
            instructions = [
                str(token) for token in statement.flatten() if not token.is_whitespace]

            # 3. Get function owner (assuming schema is the owner)
            identifiers = [
                token for token in statement.tokens if isinstance(token, Identifier)]
            owner = None
            for identifier in identifiers:
                if function_name in str(identifier):
                    owner = str(identifier).split('.')[0].strip()

            function_info.append({
                'name': function_name,
                'params': function_params,
                'instructions': instructions,
                'owner': owner
            })

    return function_info


sql_script = """
CREATE FUNCTION schema1.function1(arg1 INT, arg2 VARCHAR)
RETURNS INT AS $$
BEGIN
    -- Your SQL statements here
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION schema2.function2(arg1 INT, arg2 VARCHAR)
RETURNS INT AS $$
BEGIN
    -- Your SQL statements here
END;
$$ LANGUAGE plpgsql;
"""

function_info = extract_function_info(sql_script)
print(function_info)
