import os
from getpass import getpass

def main():
    menu()

def menu():
    while True:
        print("\n=== Password Manager ===")
        print("1. Generate a Password")
        print("2. Access the Vault")
        print("3. Store a New Credential")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            os.system('clear')
            # TODO: Generate a password, and then print to console.
        elif choice == "2":
            os.system('clear')
            # TODO: Implement password, store as hash.
        elif choice == "3":
            name = input("Enter the name of the service: ")
            username = input("Enter the username: ")
            password = getpass("Enter the password: ")
            # TODO: Store the credential in a file, store password as hash, use password generated from the function.
        elif choice == "4":
            print("Exiting the program. See you next time!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 4.")

if __name__ == "__main__":
    main()



