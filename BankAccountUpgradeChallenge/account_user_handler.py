from random import randint

char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

def user_id():
    id = ''.join(char_list[randint(0,61)] for i in range(0, 15))
    return id


def account_id():
    id = ''.join(char_list[randint(0,61)] for i in range(0, 20))
    return id


def integer_validator():
    while True:
        number = input()
        try:
            return int(number)
        except:
            print('Insert only numbers!')
