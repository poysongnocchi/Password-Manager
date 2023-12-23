

passwords = []
    # Stores user data
def insert_password(service, username, password):
    data = {"service": service, "username": username, "password": password}
    passwords.append(data)
    print("Password added successfully")


def add_passwords():
    # Get users input
    user_service = input("Eenter the service for this password: ")
    username = input("Enter the username for this service: ")
    user_password = input("Enter the password you want to save (at least 6 characters): ")

    # Shows user previously stored data
def show_passwords():
    for pw in passwords:
        print("service: " + pw["service"] + ", username: " + pw["username"] + ", password: " + pw["password"])





def main():
    while True:
        # Display Menu
        print("\nPassword Manager")
        print("1. Show Saved Passwords")
        print("2. Add New Password")
        print("3. Generate Strong Password")
        print("4. Exit App")

        choice = input("Enter your choice: ")

        # Handle users input
        if choice == '1':
            show_passwords()
        elif choice == '2':
            add_passwords()
        elif choice == '3':
            generate_password()
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")