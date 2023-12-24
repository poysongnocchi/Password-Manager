import random
import pyperclip
import pyfiglet
from colorama import Fore

ascii_banner = pyfiglet.figlet_format("Welcome to Password Manager")
print(ascii_banner)

print('\033[1m' + "Your simple tool to remember everithing you cant" + '\033[0m')
print('\033[1m' +"Store passwords for a service, check your stored passwords or generate a strong one." + '\033[0m')
print('\033[1m' +"We reccomend you to dont get hacked." + '\033[0m')

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

    # Handling User Error
    while len(user_password) < 6:
        print("Password must be atleast 6 characters: ")
        user_password = input("Enter the password you want to save: ")

    insert_password(user_service, username, user_password)

    # Shows user previously stored data
def show_passwords():
    for pw in passwords:
        print("service: " + pw["service"] + ", username: " + pw["username"] + ", password: " + pw["password"])

def get_random_char():
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyxz"
    index = random.randint(0,51) # give value to index as random number between 0-51
    random_letter = uppercase_letters[index] # give value to random_letters the character at random index
    return random_letter

def get_random_special_char():
    special_chars = "!@#$%^&*()_+"
    index = random.randint(0,11) # give value to index as random number between 0-11
    random_special = special_chars[index] # give value to random_specials the character at random index
    return random_special

def generate_password():
    random_password = "" #declare random password as empty string
    for i in range(0,12): #iterate 12 times
        random_password += get_random_char() #random character is appended to random passwords
    
    for i in range(0,4): # iterate 4 times
        random_password += get_random_special_char() #random character is appended to random passwords

    print(random_password)          
    pyperclip.copy(random_password) #gets copied automatically to clipboard
    print(Fore.CYAN + "Your password has been copied to the clipboard ")       

def main():
    while True:
        # Display Menu
        print(Fore.CYAN + "\nPassword Manager")
        print(Fore.GREEN + "1. Show Saved Passwords")
        print("2. Add New Password")
        print("3. Generate Strong Password")
        print("4. Exit App")

        choice = input(Fore.YELLOW + "Enter your choice: ")

        # Handling type error
        try:
            convert_choice = int(choice)
        except:
            print(Fore.RED + "Error, Choice must be a number") 
            continue   

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

def test():
    insert_password("abc","123","password")
    assert passwords[0]['service'] == "Gmail"
    assert passwords[0]['username'] == "Test@gmail.com"
    assert passwords[0]['password'] == "strongpassword1234"

# test() 

main()