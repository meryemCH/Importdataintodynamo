import boto3
import csv


def batch_write(table_name,rows):
    table = boto3.resource('dynamodb').Table('table_name')

    with table.batch_writer() as batch:
        for row in rows:
            batch.put_item(Item=row)
    return True

def read_csv(csv_file,list):
    rows = csv.DictReader(open('data/data.csv'))

    for row in rows:
        list.append(row)

if __name__ == '__main__':

    table_name = 'immo_data'
    file_name = 'data/data.csv'
    items = []

    read_csv(file_name,items)
    status=batch_write(table_name,items)

    if (status):
        print('Data is saved')
    else:
        print('Error while inserting data')
