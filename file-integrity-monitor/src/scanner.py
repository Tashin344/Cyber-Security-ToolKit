import os
import database
def scanning(file_path):
    if not os.path.isdir(file_path):
        print("Invalid directory path.")
        exit()

    directory_name = os.path.basename(file_path)

    data, database_file = database.database_load(directory_name)

    file_list = os.walk(file_path)

    return file_list, data, database_file