import pandas as pd
import csv

def create_csv_file(file_name, columns):
    with open(file_name, 'w', newline='') as f:
                file = csv.writer(f, quoting=1)
                file.writerow(columns)


def create_row(file_name, row):
    with open(file_name, 'a', newline='') as f:
        file = csv.writer(f, quoting=1)
        file.writerow(row)
        
        
def find_row(file_name, row_id):
    data = pd.read_csv(file_name, index_col='ID')
    return data.loc[data['ID'] == row_id]


def update_row(file_name, row_id, new_row):
    data = pd.read_csv(file_name, index_col='ID')
    for column in data.columns:
        data.loc[data['ID'] == row_id, column] = new_row[column]
    
    data.to_csv(file_name, index=True)


def delete_row(file_name, row_id):
    data = pd.read_csv(file_name, index_col='ID')
    data = data.drop(row_id)
    data.to_csv(file_name, index=True)


def csv_to_dict(file_name):
    csv_dict = csv.DictReader(open(file_name))
        
    my_dict = []
    for i in csv_dict:
        my_dict.append(i)
    return my_dict
