class BookStore:
    def __init__(self):
        self.books = {
            '1': {'title': 'Book1', 'author': 'Author1', 'price': 10, 'quantity': 5},
            '2': {'title': 'Book2', 'author': 'Author2', 'price': 15, 'quantity': 2},
            # Add more books as needed
        }

    def browse_books(self):
        for id, book in self.books.items():
            print(f"ID: {id}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}")

    def purchase_book(self, id):
        if self.books[id]['quantity'] > 0:
            self.books[id]['quantity'] -= 1
            print(f"You have purchased {self.books[id]['title']} by {self.books[id]['author']}.")
        else:
            print("Sorry, this book is out of stock.")

print("Welcome to Booknest!\n")
while True:
    action = input("What would you like to do? (Buy/Leave):  ")
    if action.lower() == 'buy':
        print("Following is the list of books available:\n")
        store = BookStore()
        store.browse_books()

        idbuy = int(input("Enter ID number of book you want to buy: "))
        if idbuy == 1:
            # Example usage for book 1:
            store.purchase_book('1')
        elif idbuy == 2:
            #Example usage for book 2:
            store.purchase_book('2')
    elif action.lower() == 'leave':
        print("Thank you. Please come again")
        break
