from datetime import date, datetime
import csv

def insert_csv_row(file_location, new_row):
    file = open(file_location, 'a', newline='')
    csv.writer(file).writerow(new_row)
    
def rewrite_csv(file_location, new_row):
    file = open(file_location, 'w', newline='')
    csv.writer(file).writerow(new_row)


class BankAccount:
    def __init__(self, account_id, funds):
        self.ACCOUNT_FIEDLS = [
            'ACCOUNT_ID',
            'EXTRACT',
            'funds',
            'last_operation_date',
            'daily_withdrawal_count'
        ]
        self.EXTRACT_FIELDS = [
            'Operation',
            'Operation value',
            'Funds before',
            'Funds after',
            'Operation time'
        ]
        self.ACCOUNT_ID = account_id
        self.ACCOUNT = f'accounts/{self.ACCOUNT_ID}.csv'
        self.EXTRACT = f'accounts/extracts/EXTRACT{self.ACCOUNT_ID}.csv'
        
        self.funds = funds
        self.last_operation_date = date.today()
        self.daily_withdrawal_count = 0
        
        
    def update_account_info_list(self):
        info_list = [
            self.ACCOUNT_ID,
            self.EXTRACT,
            self.funds,
            self.last_operation_date,
            self.daily_withdrawal_count
        ]
        
        rewrite_csv(self.ACCOUNT, self.ACCOUNT_FIEDLS)
        insert_csv_row(self.ACCOUNT, info_list)


    def validate_operation_value(self, operation_value):
        INVALID_VALUE_LAYOUT = '''Invalid value! Try again
    or enter '0' to cancel operation
    />>> '''
        while True:
            if operation_value == 0:
                break
            
            try:
                operation_value = round(float(operation_value), 2)
            except:
                operation_value = input(INVALID_VALUE_LAYOUT)
                continue
            
            if operation_value < 0:
                operation_value = input(INVALID_VALUE_LAYOUT)
                continue
            
            return operation_value
    
    
    def insert_extract_entry(self, operation_value, operation):
        if operation == 'deposit':
            funds_after = self.funds + operation_value
        else:
            funds_after = self.funds - operation_value
            
        extract_entry = [
            operation,
            operation_value,
            self.funds,
            funds_after,
            datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        ]
        insert_csv_row(self.EXTRACT, extract_entry)
    
    
    def deposit(self, deposit_value):
        deposit_value = self.validate_operation_value(deposit_value)
        if deposit_value == None:
            return
        else:
            self.insert_extract_entry(deposit_value, 'deposit')
            self.funds += deposit_value
            self.update_account_info_list()
            print('Operation completed')
        
        
    def withdrawal(self, withdrawal_value):
        withdrawal_value = self.validate_operation_value(withdrawal_value)
        if withdrawal_value == None:
            return
        
        istoday = str(self.last_operation_date) == str(date.today())
        if self.daily_withdrawal_count == 3 and istoday:
            print('Daily withdrawal limit reached')
            return
        elif not istoday:
            self.last_operation_date = date.today()
            self.daily_withdrawal_count = 0
        
        if withdrawal_value > 500.0:
            print('Withdrawal over 500 bucks are not allowed')
            return
        elif withdrawal_value > self.funds:
            print('Insuficient funds for opeartion')
            return
        else:
            self.insert_extract_entry(withdrawal_value, 'withdrawal')
            self.funds -= withdrawal_value
            self.daily_withdrawal_count += 1
            self.update_account_info_list()
            
            print('Operation completed. ' +
                  f'Remaining withdrawals: {3 - self.daily_withdrawal_count}')
        
        
    def view_extract(self):
        extract = list(csv.DictReader(open(self.EXTRACT), delimiter=','))
            
        print('_' * 79)
        print('Extract'.center(79))
        print('_' * 79)
        if extract == []:
            print('No operations performed')
        else:
            for extr in extract:
                for key in extr:
                    if key == 'Operation' or key == 'Operation time':
                        print(f'{key}: {extr[key]}')
                    else:
                        print(f'{key}: R${extr[key]}')
                print('_' * 79)
        
        print('_' * 79)
        print(f'Current funds: R$ {self.funds:.2f}'.center(79))
        print('_' * 79)
