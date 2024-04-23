from AccountObject import BankAccount as ba
from UserObject import User as usr
import csv

def menu():
    MENU = f'''{' MENU '.center(79, '=')}
    
        [1] Login
        [2] New User
        
        [0] Exit
    
    />>> '''
    
    return str(input(MENU))


def user_menu():
    MENU = f'''{' MENU '.center(79, '=')}
    
        [1] Sign In Account
        [2] New Account
        [3] List Accounts
        
        [4] Log Out
        [5] Delete User
        [0] Exit
    
    />>> '''
    
    return str(input(MENU))


def account_menu():
    MENU = f'''{' MENU '.center(79, '=')}
    
        [1] Deposit
        [2] Withdrawal
        [3] View Extract
        
        [4] Quit Account
        [5] Delete Account
        
        [0] Exit
        
    />>> '''


def main():
    while True:
        option = menu()
        
        if option == '1':
            option = user_menu()


main()
