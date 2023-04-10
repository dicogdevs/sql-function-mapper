# This is a sample Python script.
import sql_function_mapper

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instructions = [
        'SELECT', 'INSERT', 'DELETE', 'UPDATE', 'COPY', 'EXEC',
        'ALTER', 'DROP', 'TRUNCATE', 'LOCK', 'GRANT',
        'REVOKE', 'REPLACE', 'SECURITY DEFINER', 'CREATE'
    ]
    result = sql_function_mapper.sql_function_mapper(
        './file.sql', instructions, '')
    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
