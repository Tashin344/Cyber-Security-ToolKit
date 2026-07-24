import hashing
import update_database
import os



def compare(file_list, data, current_files):
    valid_files=0
    invalid_files=0
    new_files=0

    for current_folder, subfolders, files in file_list:

        for filename in files:
            
            print(filename)
            
            full_path = os.path.join(current_folder, filename)
            with open(full_path, "rb") as file: 
                
                content = file.read()
                hash_value = hashing.hashing(content)
            current_files.add(full_path)
            if(full_path in data):

                
                if(data[full_path] == hash_value):
                    print("VALID ✅")
                    valid_files=valid_files + 1
                else:
                    print("INVALID ❌")
                    invalid_files=invalid_files + 1
                    print("Would you like to update the database? (y/n)")
                    choice = input().lower()
                    if choice == 'y':
                        print("Database updated")
                        update_database.update_database(hash_value, full_path, data)
                    else:
                        print("Database not updated.")     
            else:
                print("New File created")
                print("Baseline value has been added")
                new_files=new_files + 1
                update_database.update_database(hash_value, full_path, data)

    return valid_files, invalid_files, new_files
    