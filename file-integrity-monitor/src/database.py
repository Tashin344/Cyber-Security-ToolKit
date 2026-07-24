
import os
import json

def database_load(directory_name):
    os.makedirs("databases", exist_ok=True)
    
    database_file = os.path.join("databases", directory_name + ".json")
    if os.path.exists(database_file):  
        with open(database_file, "r") as file:
             data = json.load(file)
            
    else:
        data = {}

    return data, database_file