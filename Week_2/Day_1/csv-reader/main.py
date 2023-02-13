import csv

def find_dog():
    with open('./data/dogs.csv', newline='') as dog_db:
        read_data = csv.reader(dog_db, delimiter = ',', quotechar='|')
        for row in read_data:
            if row[0] == 'name':
                continue
            else:
                print(f'{row[0]} is a{row[1]} year old{row[2]}')
        
def find_cat():
     with open('./data/cats.csv', newline='') as cat_db:
        read_data = csv.reader(cat_db, delimiter = ',', quotechar='|')
        for row in read_data:
            if row[0] == 'name':
                continue
            else:
                print(f'{row[0]} is a{row[1]} year old{row[2]}')

def animal_db_chk(animal):
    available_animals = ['cats', 'dogs']

    if animal in available_animals:
        return True
    
    return False
    

def main():
    animal = input("What species are you looking for? ").lower()

    if not animal_db_chk(animal) is True:
        raise Exception("Animal unavailable or improper input. Check your spelling and try again!")
        
    animal_db_chk(animal) == True
    
    if animal == 'cats':
        find_cat()
    if animal == 'dogs':
        find_dog()
    
main()