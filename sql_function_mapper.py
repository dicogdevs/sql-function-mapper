import sql_function_parser
import sql_file_reader


def sql_function_mapper(input_path: str, instructions, output_path: str):
    sql = sql_file_reader.sql_file_reader(input_path)
    return sql_function_parser.sql_function_parser(sql, instructions)
