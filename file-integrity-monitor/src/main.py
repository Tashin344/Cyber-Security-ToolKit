
import json 
import user_input
import compare
import deletion   
import scanner 
import reports

file_path = user_input.take_input()  

file_list, data, database_file = scanner.scanning(file_path)
print("----Files In The Directory----")

current_files = set() 
valid_files, invalid_files, new_files = compare.compare(file_list, data, current_files)

  

files_to_delete = []
deletion.delete(data, current_files, files_to_delete)


with open (database_file, "w") as file:
        json.dump(data, file)

reports.reporting(file_path, files_to_delete, valid_files, invalid_files, new_files)