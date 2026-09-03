def add_book(book_id, title, author):
    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},Available\n")

def read_all_books():
    books = []
    if not os.path.exists("books.txt"):
        return books
    with open("books.txt", "r") as f:
        for line in f:
            bid, title, author, status = line.strip().split(",")
            books.append({"id": bid, "title": title, "author": author, "status": status})
    return books

def save_books(books):
    with open("books.txt", "w") as f:
        for b in books:
            f.write(f"{b['id']},{b['title']},{b['author']},{b['status']}\n")

def search_book(title):
    for b in read_all_books():
        if b["title"].lower() == title.lower():
            return b
    return None

def update_status(book_id, status):
    books = read_all_books()
    for b in books:
        if b["id"] == book_id:
            b["status"] = status
    save_books(books)

def display_available():
    print("\nAvailable Books:")
    for b in read_all_books():
        if b["status"] == "Available":
            print(f"{b['id']} | {b['title']} by {b['author']}")

if os.path.exists("books.txt"):
    os.remove("books.txt")

add_book("B1", "Let Us Python", "Yashavant Kanetkar")
add_book("B2", "Fluent Python", "Luciano Ramalho")
update_status("B1", "Issued")
display_available()
print("Search Result:", search_book("Fluent Python"))
