library = {}

def add_book(book_id, name):
    library[book_id] = {'name': name, 'available': True}

def issue_book(book_id):
    if book_id in library and library[book_id]['available']:
        library[book_id]['available'] = False
        return True
    return False

def return_book(book_id):
    if book_id in library:
        library[book_id]['available'] = True

def search_book(name):
    for book_id, details in library.items():
        if details['name'].lower() == name.lower():
            return book_id, details
    return None

def display_available():
    return {bid: details['name'] for bid, details in library.items() if details['available']}

add_book(101, "Python Programming")
add_book(102, "Data Structures")
issue_book(101)
print("Available Books:", display_available())
