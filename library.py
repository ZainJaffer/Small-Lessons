import json

def save_library(library):
    with open('data.json', 'w') as file:
        json.dump(library, file)

def load_library():
    with open('data.json', 'r') as file:
        library = json.load(file)
        return library

load_library()

library = {
    "Harry Potter and the Philosopher's Stone": {
        "author": "J.K. Rowling",
        "year": 1997,
        "genre": "Fantasy"
    },
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "year": 1960,
        "genre": "Classic Fiction"
    },
    "1984": {
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian"
    },
    "Pride and Prejudice": {
        "author": "Jane Austen",
        "year": 1813,
        "genre": "Romance"
    },
    "The Great Gatsby": {
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Classic Fiction"
    },
    "Zain": {
        "author": "Zain",
        "year": 1925,
        "genre": "Classic Fiction"
    }
}



def add():
    title = input("Please choose title of book").title()
    author = input("Please choose author of book")
    year = int(input("Please choose year of book"))
    genre = input("Please choose genre of book")
    library[title] = {'author': author, 'year' : year, 'genre' : genre}
    print(f"{title} has been added")

def view():
    for key, values in library.items():
        print(key, values)
        print()

def remove():
    title = input("Please select book to delete").title()
    if title in library:
        del library[title]
        print(f"{title} deleted")
    else: print("Sorry title not found")

def update():
    title = input("Please select book to modify").title()
    fields = ['author','year','genre']
    if title in library:
        print(f"More information on the book \n: {title}, by {library[title]['author']}, {library[title]['year']}, {library[title]['genre']} ")        
        choice = input("Please select the selection you wish to modify: title, author, year or genre").lower()
        if choice in fields:
            change = input("Please select the new data to write over the existing data")
            library[title][choice] = change
        elif choice == 'title':
            change = input("Please select the new data to write over the existing data")
            library[change] = library.pop(title)
        else:
            print("Sorry this field is not recognized")
    else: print("Sorry this book doesn't exist in the library")


view()
