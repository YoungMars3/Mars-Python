# Action 1: Browse Books
def browse_books(self):
    # This method prints all books available in the bookstore's inventory.
    for id, book in self.books.items():
        print(f"ID: {id}, Title: {book['title']}, - Author: {book['author']} 🔹 Genre: {book['genre']} 🔹 Price: ${book['price']} 🔹 Quantity: {book['quantity']}")

# Action 2: Search Books
def user_search_books(self, search_term):
    # This method searches for books by title or author that match the given search term.
    # If matches are found, it prints each book's details and shows the cover image.
    for id, book in self.books.items():
        if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower():
            print(f"ID: {id}, Title: {book['title']}, Author: {book['author']}, Price: ${book['price']}, Quantity: {book['quantity']}")
            self.show_cover_image(book['title'])

# Helper Method: Show Cover Image
def show_cover_image(self, title):
    # This helper method attempts to show the cover image of a book based on its title.
    img_path = f'C:\\Users\\User\\PycharmProjects\\MyBS\\book_cover\\{title.lower().replace(" ", "_")}.jpg'
    try:
        img = Image.open(img_path)
        img.show()
    except FileNotFoundError:
        print(f"\nCover image not found for {title}.")

# Action 3: Add to Cart
def purchase_book(self, id):
    # This method allows the user to add a book to the shopping cart by its ID.
    # It checks the stock and if available, adds the book to the cart and decreases the stock quantity.
    if self.books[id]['quantity'] > 0:
        self.books[id]['quantity'] -= 1
        print(f"\nYou have added {self.books[id]['title']} by {self.books[id]['author']} to your shopping cart.")
        self.shopping_cart[id] = self.shopping_cart.get(id, 0) + 1
    else:
        print("\nSorry, this book is out of stock.")
