FILE_NAME = "vault"

def initialize_file():
    try:
        with open(FILE_NAME, "x") as file:
            file.write("Name | Username | Password\n")
    except FileExistsError:
        pass
initialize_file()    

def add_record(name, username, password):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name} | {username} | {password}\n")
    print("Record added successfully.")
        
def remove_record(name):
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        with open(FILE_NAME, "w") as file:
            found = False
            for line in lines:
                if not line.startswith(name):
                    file.write(line)
                else:
                    found = True 
            if found:
                print("Record deleted succesfully.")
            else:
                print("Record not found.")
    except FileNotFoundError:
        print("No record found.")

def viewRecord():
    print("List of Credentials Stored:")
    try:
        with open(FILE_NAME, "r") as file :
            isi = file.read()
            print(isi)
    except FileNotFoundError:
        print("There is no file found")    
        
def searchRecord(name):
    try:
        with open (FILE_NAME, "r") as file:
            for baris in file:
                if name in baris:
                    print("Record found:", baris.strip())
                    return
        print(f"No record with {name} was not found")
    except FileNotFoundError:
        print("There is no file found")
