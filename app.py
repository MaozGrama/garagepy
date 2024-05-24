from enum import Enum
from icecream import ic
import json

# Define the file path for saving the data
file_path = "cars.json"

# Initialize the Cars list, potentially loading from a file
def load_from_file():
    try:
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

Cars = load_from_file()

class Actions(Enum):
    ADD = 1
    REMOVE = 2  
    UPDATE = 3
    INFO = 4
    COUNT = 5
    EXIT = 6

def save_to_file():
    with open(file_path, 'w') as json_file:
        json.dump(Cars, json_file, indent=4)

def menu():
    for action in Actions:
        print(f'{action.value} - {action.name}')
    return Actions(int(input("Choose your selection: ")))

def add():
    Cars.append({
        'cModel': input('Car model: '), 
        'cColor': input("What's the color of the car? "), 
        'CustomerName': input("What's your name? ")
    })
    save_to_file()

def remove():
    index = int(input("Enter the index of the car to remove: "))
    if 0 <= index < len(Cars):
        del Cars[index]
        save_to_file()
    else:
        print("Invalid index")

def update():
    index = int(input("Enter the index of the car to update: "))
    if 0 <= index < len(Cars):
        Cars[index] = {
            'cModel': input('New car model: '), 
            'cColor': input("New car color: "), 
            'CustomerName': input("New customer name: ")
        }
        save_to_file()
    else:
        print("Invalid index")

def info():
    for index, Car in enumerate(Cars):
        print(f"({index}) cModel: {Car['cModel']} , cColor: {Car['cColor']}, CustomerName: {Car['CustomerName']}")

def count():
    print(f"Total number of cars: {len(Cars)}")

if __name__ == "__main__":
    while True:
        user_selection = menu()
        if user_selection == Actions.ADD:
            add()
        elif user_selection == Actions.REMOVE:
            remove()
        elif user_selection == Actions.UPDATE:
            update()
        elif user_selection == Actions.INFO:
            info()
        elif user_selection == Actions.COUNT:
            count()
        elif user_selection == Actions.EXIT:
            exit()
