# Defining a class named BookStore
class BookStore:
    def __init__(self):
        self.authors = self.load_authors()
        self.books = self.load_books()

    # Reading author names from "author_names.txt"
    def load_authors(self):
        with open('author_names.txt', 'r') as file:
            return [line.strip() for line in file]

    # Reading book names from "book_names.txt"
    def load_books(self):
        # Load book names and quantities from the file
        with open('book_names.txt', 'r') as file:
            book_data = [line.strip().split(',') for line in file]

        # Create a dictionary with book IDs, names, and quantities
        books = {}
        for i, (name, quantity_str) in enumerate(book_data, start=1):
            # Use the corresponding author for each book
            author = self.authors[i - 1] if i <= len(self.authors) else 'Unknown Author'
            books[str(i)] = {'title': name, 'author': author, 'price': 10 + i, 'quantity': int(quantity_str)}
        return books

    # Displaying info bout all the books in directory
    def browse_books(self):
        for id, book in self.books.items():
            print(f"ID: {id}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}")

    #  Looking for search terms
    def search_books(self, search_term):
        for id, book in self.books.items():
            if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower():
                print(f"ID: {id}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}")

    # Checking for availability and purchasing book
    def purchase_book(self, id):
        if self.books[id]['quantity'] > 0:
            self.books[id]['quantity'] -= 1
            print(f"\nYou have purchased {self.books[id]['title']} by {self.books[id]['author']}.")
        else:
            print("\nSorry, this book is out of stock.")


# Output starts from here:
print("Welcome to Booknest.")
store = BookStore()

# Choosing whether to buy or leave
while True:
    action = input("\nWhat would you like to do? (Buy/Leave):  ")

    #Printing names of all the books with details
    if action.lower() == 'buy':
        print("\nFollowing is the list of books available:")
        store.browse_books()

    #Prompt to enter the ID number of a book
        idbuy = input("\nEnter ID number of book you want to buy: ")

        if idbuy in store.books:
            store.search_books(store.books[idbuy]['title'])
            store.purchase_book(idbuy)
        else:
            print("\nInvalid ID. Please choose a valid book ID.")

    elif action.lower() == 'leave':
        print("\nThank you. Please come again")
        break