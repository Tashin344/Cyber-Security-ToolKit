
import time
import os

def reporting(file_path, files_to_delete, valid_files, invalid_files, new_files):
    print("==================================")
    print("FILE INTEGRITY MONITOR REPORT")
    print("==================================")
    print()

    print("Directory Scanned:", file_path)
    print()

    print("Scan Time: ")
    print()
    print(time.ctime())
    print()
    print("Summary of Scan Results:")
    print()

    print("Total Files Scanned: ", valid_files + invalid_files + new_files)
    print()
    print("Valid Files: ", valid_files)
    print()
    print("Invalid Files: ", invalid_files)
    print()
    print("New Files: ", new_files)
    print()

    print("Files Deleted: ", len(files_to_delete))

    os.makedirs("Reports", exist_ok=True)
          
    with open("Reports/report.txt", "w") as f:
        print("==================================", file=f)
        print("FILE INTEGRITY MONITOR REPORT", file=f)
        print("==================================", file=f)
        print(file=f)

        print("Directory Scanned:", file_path, file=f)
        print(file=f)

        print("Scan Time: ", file=f)
        print(file=f)
        print(time.ctime(), file=f)
        print(file=f)
        print("Summary of Scan Results:", file=f)
        print(file=f)

        print("Total Files Scanned: ", valid_files + invalid_files + new_files, file=f)
        print(file=f)
        print("Valid Files: ", valid_files, file=f)
        print(file=f)
        print("Invalid Files: ", invalid_files, file=f)
        print(file=f)
        print("New Files: ", new_files, file=f)
        print(file=f)

        print("Files Deleted: ", len(files_to_delete), file=f)