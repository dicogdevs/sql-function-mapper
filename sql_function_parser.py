import sqlparse
from map_functions import map_functions


def sql_function_parser(sql: str, instructions):
    parsed_sql = sqlparse.parse(sql)
    return map_functions(parsed_sql, instructions)
