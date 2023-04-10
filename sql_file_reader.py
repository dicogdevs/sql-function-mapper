def sql_file_reader(sql_file_path):
    with open(sql_file_path, 'r') as file:
        return file.read()
