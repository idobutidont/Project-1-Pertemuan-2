import os
import vault
import generator

def main():
    os.system('clear')
    menu()

def menu():
    while True:
        print("\n=== Password Manager ===")
        print("1. Generate a Password")
        print("2. Access the Vault")
        print("3. Store a New Credential")
        print("4. Delete a Credential")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            os.system('clear')
            generator.print_password()
            # TODO: Generate a password, and then print to console.
            
        elif choice == "2":
            os.system('clear')
            vault.viewRecord()
            # TODO: Implement password, store as hash.
            
        elif choice == "3":
            os.system('clear')
            name = input("Enter the name of the service: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            os.system('clear')
            vault.add_record(name, username, password)
        
        elif choice == "4":
            os.system('clear')
            name = input("Enter the name of the service: ")
            vault.remove_record(name)
            
        elif choice == "5":
            print("Exiting the program. See you next time!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()