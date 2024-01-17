#pip install Pillow
from PIL import Image

# Defining a class named BookStore
class BookStore:
    #Initializing BookStore object
    def __init__(self):
        self.authors = self.load_authors()
        self.books = self.load_books()
        self.shopping_cart = {} # Dictionary to store details of added books
        self.users = {}  # Dictionary to store user credentials

    # Reading author names from "author_names.txt"
    def load_authors(self):
        with open('author_names.txt', 'r') as file:
            return [line.strip() for line in file]

    # Reading book names from "books.txt"
    def load_books(self):
        with open('books.txt', 'r') as file:
            # Read each line, strip trailing whitespaces, and split the line into a list using commas
            book_data = [line.strip().split(',') for line in file]

        books = {}
        # Iterate over the enumerated book_data, where each element is a list representing book details
        for i, (name, genre, price_str, quantity_str) in enumerate(book_data, start=1):
            # Determine the author based on the index i, considering self.authors list
            author = self.authors[i - 1] if i <= len(self.authors) else 'Unknown Author'
            # Create a dictionary entry for each book, using a string representation of the index as the key
            books[str(i)] = {'title': name, 'author': author, 'genre': genre, 'price': int(price_str), 'quantity': int(quantity_str)}
        return books

    def browse_books(self):
        for id, book in self.books.items():
            print(f"ID: {id}, Title: {book['title']}, - Author: {book['author']} 🔹 Genre: {book['genre']} 🔹 Price: ${book['price']} 🔹 Quantity: {book['quantity']}")

    #  Looking for search terms
    def user_search_books(self, search_term):
        for id, book in self.books.items():
            if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower():
                print(f"ID: {id}, Title: {book['title']}, Author: {book['author']}, Price: ${book['price']}, Quantity: {book['quantity']}")
                self.show_cover_image(book['title'])

    def search_books(self, search_term):
        found_books = [id for id, book in self.books.items() if
                       search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]

        if not found_books:
            print(f"\nSearched term '{search_term}' not found.")
        else:
            for id in found_books:
                book = self.books[id]
                print(
                    f"ID: {id}, Title: {book['title']}, Author: {book['author']}, Price: ${book['price']}, Quantity: {book['quantity']}")
                self.show_cover_image(book['title'])

    # Show the cover image based on the book title
    def show_cover_image(self, title):
        img_path = f'C:\\Users\\User\\PycharmProjects\\Python_Group3\\book_cover\\{title.lower().replace(" ", "_")}.jpg'
        try:
            img = Image.open(img_path)
            img.show()
        except FileNotFoundError:
            print(f"\nCover image not found for {title}.")

    # Checking for availability and purchasing book
    def purchase_book(self, id):
        if self.books[id]['quantity'] > 0:
            self.books[id]['quantity'] -= 1
            print(f"\nYou have added {self.books[id]['title']} by {self.books[id]['author']} to your shopping cart.")
            self.shopping_cart[id] = self.shopping_cart.get(id, 0) + 1
        else:
            print("\nSorry, this book is out of stock.")

    # View the items in the shopping cart
    def view_shopping_cart(self):
        print("\nYour Shopping Cart:")
        for id, quantity in self.shopping_cart.items():
            book = self.books[id]
            print(f"ID: {id}, Title: {book['title']}, Author: {book['author']}, Quantity: {quantity}")

    # Checkout and finalize the purchase
    def checkout(self):
        total_price = 0
        for id, quantity in self.shopping_cart.items():
            book = self.books[id]
            total_price += book['price'] * quantity
            book['quantity'] -= quantity

        print(f"\nTotal Price: ${total_price}")
        print("Thank you for your purchase!")
        self.shopping_cart = {}  # Clear the shopping cart after checkout

    # User registration
    def register_user(self, username, password):
        if username not in self.users:
            self.users[username] = {'password': password}
            print(f"\nUser {username} registered successfully.")
        else:
            print(f"\nUsername {username} is already taken. Please choose a different username.")

    # User login
    def login_user(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            print(f"\nWelcome, {username}!")
            return True
        else:
            print("\nInvalid username or password. Please try again.")
            return False

# Output starts from here:
print("Welcome to BOOKHEAVEN 😀")
store = BookStore()

while True:
    option = input("Selct an option (1-Log in | 2-Create an account | 3-Shutdown program): ")

    if option == '1':
        # User login
        while True:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            if store.login_user(username, password):
                break  # Break out of the login loop if successful
            else:
                retry_option = input(
                    "\nWould you like to:\n1. Retry login\n2. Create an account\n3. Leave\nEnter your choice (1-3): ")
                if retry_option == '2':
                    # Break out of the login loop and go to account creation
                    while True:
                        username = input("\nCreate a username: ")
                        password = input("Create a password: ")
                        store.register_user(username, password)
                        break  # For simplicity, break after one registration
                        exit()
                elif retry_option == '3':
                    # Break out of the login loop and go to the main options
                    print("\nPower Off 😴")
                    break
                    exit()

    elif option == '2':
        # User registration
        while True:
            username = input("\nCreate a username: ")
            password = input("Create a password: ")
            store.register_user(username, password)
            break  # For simplicity, break after one registration

    elif option == '3':
        print("\nPower Off 😴")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.")

    # Choosing options
    while True:
        action = input("\nChoose an action (1-Browse | 2-Search | 3-Add to cart | 4-View cart | 5-Check Out | 6-Log Out):  ")

        #Browse
        if action == '1':
            print("\nFollowing is the list of books available:")
            store.browse_books()

        #Search
        elif action == '2':
            search_term = input("Enter the title or author you want to search: ")
            store.user_search_books(search_term)

        #Add to cart
        elif action == '3':
            idbuy = input("Enter ID number of book you want to add to your shopping cart: ")
            if idbuy in store.books:
                store.purchase_book(idbuy)
            else:
                print("\nInvalid ID. Please choose a valid book ID.")

        #View cart
        elif action == '4':
            store.view_shopping_cart()

        #Check out
        elif action == '5':
            store.checkout()

        #Leave
        elif action == '6':
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6")