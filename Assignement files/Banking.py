import os
import time

# Sample user data (Account Number: PIN)
user_data = {"123456": {"pin": "1234", "balance": 1000}}

# Function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Welcome Screen
def welcome_screen():
    clear_screen()
    print("*************************************")
    print("*  Welcome to the UCB, Birmingham ATM!      *")
    print("*  Developed by: RP Wadhwa        *")
    print("*  Year of Release: 2025           *")
    print("*************************************")
    input("\nPress Enter to continue...")
    clear_screen()

# Function to log in
def login():
    clear_screen()
    print("***** Secure Login *****")
    
    for attempt in range(3):  # Allow 3 login attempts
        account_number = input("\nEnter Account Number: ").strip()
        pin = input("Enter PIN: ").strip()

        if account_number in user_data and user_data[account_number]["pin"] == pin:
            print("\nLogin successful! ✅")
            time.sleep(1)
            return account_number  # Return the logged-in account number
        else:
            print("\nInvalid Account Number or PIN. ❌ Try again.")
    
    print("\nToo many failed attempts. Exiting for security reasons.")
    exit()

# Function to check balance
def check_balance(account_number):
    clear_screen()
    print("***** Account Balance *****")
    print(f"Your current balance is: £{user_data[account_number]['balance']}")
    input("\nPress Enter to return to the menu...")
    clear_screen()

# Function to deposit money
def deposit_money(account_number):
    clear_screen()
    print("***** Deposit Money *****")
    
    while True:
        try:
            amount = float(input("\nEnter deposit amount: £"))
            if amount <= 0:
                print("\nInvalid amount! Please enter a positive number.")
            else:
                user_data[account_number]["balance"] += amount
                print(f"\nDeposit successful! ✅ Your new balance is: £{user_data[account_number]['balance']}")
                break
        except ValueError:
            print("\nInvalid input! Please enter a numeric value.")
    
    input("\nPress Enter to return to the menu...")
    clear_screen()

# Function to withdraw money
def withdraw_money(account_number):
    clear_screen()
    print("***** Withdraw Money *****")
    
    while True:
        try:
            amount = float(input("\nEnter withdrawal amount: £"))
            if amount <= 0:
                print("\nInvalid amount! Please enter a positive number.")
            elif amount > user_data[account_number]["balance"]:
                print("\nInsufficient funds! ❌ Please enter a lower amount.")
            else:
                user_data[account_number]["balance"] -= amount
                print(f"\nWithdrawal successful! ✅ Your new balance is: £{user_data[account_number]['balance']}")
                break
        except ValueError:
            print("\nInvalid input! Please enter a numeric value.")
    
    input("\nPress Enter to return to the menu...")
    clear_screen()

# Function to change PIN
def change_pin(account_number):
    clear_screen()
    print("***** Change PIN *****")

    old_pin = input("\nEnter your current PIN: ").strip()

    if old_pin == user_data[account_number]["pin"]:
        new_pin = input("\nEnter new PIN: ").strip()
        confirm_pin = input("Confirm new PIN: ").strip()

        if new_pin == confirm_pin:
            user_data[account_number]["pin"] = new_pin
            print("\nPIN successfully changed! ✅")
        else:
            print("\nError: PINs do not match. ❌ Try again.")
    else:
        print("\nIncorrect current PIN! ❌")
    
    input("\nPress Enter to return to the menu...")
    clear_screen()

# Main Menu
def main_menu(account_number):
    while True:
        print("***** MAIN MENU *****")
        print("1) Check Balance")
        print("2) Deposit Money")
        print("3) Withdraw Money")
        print("4) Change PIN")
        print("5) Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            check_balance(account_number)
        elif choice == "2":
            deposit_money(account_number)
        elif choice == "3":
            withdraw_money(account_number)
        elif choice == "4":
            change_pin(account_number)
        elif choice == "5":
            print("\nThank you for using UCB, Birmingham ATM! Have a great day. 😊")
            exit()
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

# Run the ATM System
welcome_screen()
user_account = login()
main_menu(user_account)
