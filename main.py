from authentication import register, login, reset_password
from game_Result import find_game_deals
import validations

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Reset Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                nested_menu()
        elif choice == '3':
            reset_password()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

def nested_menu():
    while True:
        print("\n=== Game Comparison Menu ===")
        print("1. Search for a game")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            find_game_deals()
        elif choice == '2':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
