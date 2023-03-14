import csv

def display_csv_reader():
    with open('monster.csv') as f:
        reader = csv.reader(f, delimeter=',')
        for row in reader:
            print(row[1])
            
            
def display_csv_reader_dict():
    with open('monsters.csv') as f:
        dictReader = csv.DictReader(f, delimeter=',')
        for row in dictReader:
            print(row["monsterName"] + "is priced at " + row["price"])
            
            
            
if __name__ == '__main__':
    display_csv_reader()
    display_csv_reader_dict()