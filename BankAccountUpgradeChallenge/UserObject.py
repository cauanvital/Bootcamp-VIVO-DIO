import account_user_handler
import csv_controller as ct

class User:
    def __init__(self,id=None, *, cpf, username, email, password):
        self.ID = account_user_handler.user_id() if id == None else id
        self.cpf = cpf
        self.username = username
        self.email = email
        self.password = password
        self.ACCOUNTS_FILE = f'accounts/{self.ID}_accounts.csv'
        
        if id == None:
            user_info = [
                self.ID,
                self.cpf,
                self.username,
                self.email,
                self.password
            ]
            
            ACCOUNT_FIEDLS = [
                'ID',
                'ACCOUNT NUMBER',
                'FUNDS',
                'LAST OPERATION DATE',
                'REMAINING WITHDRAWAL'
            ]
            
            ct.create_row('users.csv', user_info)
            ct.create_csv_file(self.ACCOUNTS_FILE, ACCOUNT_FIEDLS)
    
    
    def list_accounts(self):
        account_list = ct.csv_to_dict(self.ACCOUNTS_FILE)
        if account_list == []:
            print('_' * 79)
            print('No accounts found')
        else:
            for acc in account_list:
                print('_' * 79)
                print(f'ACCOUNT NUMBER: {acc['ACCOUNT NUMBER']}')
                print(f'FUNDS: ${acc['FUNDS']}')
                print(f'LAST OPERATION DATE: {acc['LAST OPERATION DATE']}')
                print(f'REMAINING WITHDRAWAL: {acc['REMAINING WITHDRAWAL']}')
                print(f'ID: {acc['ID']}')
                
    
    def new_account(self):
        account_number = 'a'
        

    def delete_account(self, account_to_delete_id):
        while True:
            sure = str(input('Are you sure? (y/n)  ')).lower()
            if sure == 'y' or sure == 'yes':
                ct.delete_row(self.ACCOUNTS_FILE, account_to_delete_id)
            elif sure == 'n' or sure == 'no':
                break
            else:
                print('INVALID OPTION! Try again...')
