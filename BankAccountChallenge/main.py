from bankaccountobject import BankAccount as ba
import csv

def initial_menu():
    INITIAL_MENU = f'''{' MENU '.center(79, '=')}
    
        [1] Login
        [2] New Account
        [3] List Accounts
        
        [0] Exit
    
    />>> '''
    
    return str(input(INITIAL_MENU))


def menu():
    MENU = f'''{' MENU '.center(79, '=')}
    
        [1] New Account
        [2] List Accounts
        
        [3] Deposit
        [4] Withdrawal
        [5] View Extract
        [6] Log Out
        
        [0] Exit
    
    />>> '''
    
    return str(input(MENU))


def insert_float_value(value):
    while True:
        try:
            value = float(value)
            break
        except:
            print('Invalid value. Try again...')
            value = input('    />>>')
            continue
        
    return value


def insert_csv_row(file_location, new_row):
    file = open(file_location, 'a', newline='')
    csv.writer(file).writerow(new_row)
    
    
def login():
    users_id_list = open('users_id.txt', 'r').read().split('\n')
    INSERT_LOGIN_ID_LAYOUT = '''\nInsert your account ID
    or enter '0' to cancel operation
    />>> '''
    while True:
        login_id = str(input(INSERT_LOGIN_ID_LAYOUT))
        if login_id == '0':
            break
        elif login_id not in users_id_list:
            print('Account don\'t exists')
        else:
            logged_account_file = open(f'accounts/{login_id}.csv', newline='')
            account_info_list = list(csv.reader(logged_account_file))
            account_info = account_info_list[1]
            
            current_value_1 = float(account_info[2])
            logged_account = ba(login_id, current_value_1)
            
            current_value_2 = account_info[3]
            logged_account.last_operation_date = current_value_2
            
            current_value_3 = int(account_info[4])
            logged_account.daily_withdrawal_count = current_value_3
            
            return logged_account


def new_account():
    INSERT_ID_LAYOUT = '''\nInsert an ID to the new account
    or enter '0' to cancel operation
    />>> '''
    INSERT_FUNDS_LAYOUT = '''\nInsert the account funds
    or enter '0' to cancel operation
    />>> '''
    while True:
        users_id_list = open('users_id.txt', 'r').read().split('\n')
        id_new_account = str(input(INSERT_ID_LAYOUT))
        
        try:
            int(id_new_account)
        except:
            print('Only numbers are allowed for ID')
            continue
        
        if id_new_account == '0':
            break
        elif id_new_account in users_id_list:
            print('ID in use')
            continue
        else:
            open('users_id.txt', 'a').write(f'{id_new_account}\n')
            
            account_funds = insert_float_value(input(INSERT_FUNDS_LAYOUT))
            if account_funds == 0:
                break
            
            new_account = ba(id_new_account,account_funds)
            
            new_account_values = [
                new_account.ACCOUNT_ID,
                new_account.EXTRACT,
                new_account.funds,
                new_account.last_operation_date,
                new_account.daily_withdrawal_count
            ]
            
            insert_csv_row(new_account.ACCOUNT, new_account.ACCOUNT_FIEDLS)
            insert_csv_row(new_account.ACCOUNT, new_account_values)
            insert_csv_row(new_account.EXTRACT, new_account.EXTRACT_FIELDS)
            
            print('Account created')
            break
        

def list_accounts():
    users_id_list = open('users_id.txt', 'r').read().split('\n')
    print(f'\n{' EXISTING ACCOUNTS '.center(79, '=')}')
    for i in users_id_list:
        print(f'        {i}')
        

def logged_actions(logged_account):
    INSERT_DEPOSIT_LAYOUT = '''Insert deposit value
    or enter '0' to cancel operation
    />>> '''
    
    INSERT_WITHDRAWAL_LAYOUT = '''Insert deposit value
    or enter '0' to cancel operation
    />>> '''
    
    while True:
        option = menu()
                
        if option == '0': # exit code
            exit()
        elif option == '1': # create new account
            new_account()
        elif option == '2': # list all existing accounts
            list_accounts()
        elif option == '3': # deposit
            operation_value = input(INSERT_DEPOSIT_LAYOUT)
            if str(operation_value) == '0':
                continue
            logged_account.deposit(operation_value)
        elif option == '4': # withdrawal
            operation_value = input(INSERT_WITHDRAWAL_LAYOUT)
            if str(operation_value) == '0':
                continue
            logged_account.withdrawal(operation_value)
        elif option == '5': # view extract
            logged_account.view_extract()
        elif option == '6': # log out
            break
        else:
            print('INVALID OPTION. TRY AGAIN...')
            continue
    
    
def main():
    while True:
        option = initial_menu()
        
        if option == '0': # exit code
            exit()
        elif option == '1': # login
            users_id_list = open('users_id.txt', 'r').read().split('\n')
            if users_id_list[0] == '':
                print('No accounts created')
                continue
            logged_account = login()
            logged_actions(logged_account)
        elif option == '2': # create new account
            new_account()
        elif option == '3': # list all existing accounts
            users_id_list = open('users_id.txt', 'r').read().split('\n')
            if users_id_list[0] == '':
                print('No accounts created')
                continue
            list_accounts()
        else:
            print('INVALID OPTION. TRY AGAIN...')
            continue


main()
