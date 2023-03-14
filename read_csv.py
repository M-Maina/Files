import csv
import pandas as pd



def display_csv_reader():
    with open('monster.csv') as f:
        reader = csv.reader(f, delimeter=',')
        for row in reader:
            print(row[1])
            
            
def display_csv_reader_dict():
    with open('monster.csv') as f:
        dictReader = csv.DictReader(f, delimeter=',')
        for row in dictReader:
            print(row["monsterName"] + "is priced at " + row["price"])
            
            
def display_csv_pandas():
    df = pd.read_csv('monster.csv')
    print(df)
            
            
            
if __name__ == '__main__':
    display_csv_reader()
    display_csv_reader_dict()