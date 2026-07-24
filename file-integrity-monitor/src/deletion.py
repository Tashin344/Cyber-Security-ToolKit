

def delete(data, current_files, files_to_delete):
    for i in data:

        if(i not in current_files):
            print(f"{i} is Deleted!")
            print()
            print("Would you like to Delete it from the database? (y/n)")
            choice = input().lower()
            if choice == 'y':
                print()
                print("FILE DELETED FROM DATABASE")
                
                files_to_delete.append(i)
            else:
                print()
                print("Deleted Database Reserved")

    for i in files_to_delete:
        del data[i]