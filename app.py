from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Define the User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    

# Book catalog with IDs added
book_catalog = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian', 'price': '10.99', 'cover': 'https://i.postimg.cc/k4VBVNBd/1984.jpg'},
    {'id': 2, 'title': 'Anxious People', 'author': 'Fredrik Backman', 'genre': 'Fiction', 'price': '15.99', 'cover': 'https://i.postimg.cc/8zt5tXvS/anxious-people.jpg'},
    {'id': 3, 'title': 'Enjoy Your Life', 'author': 'Dr. Muhammad Abd Al-Rahman', 'genre': 'Self-help', 'price': '12.99', 'cover': 'https://i.postimg.cc/sgcBbDtb/enjoy-your-life.jpg'},
    {'id': 4, 'title': 'Golden Words', 'author': '  Abdul Malik Mujahid', 'genre': 'Quotes', 'price': '8.99', 'cover': 'https://i.postimg.cc/4nRZxVhw/golden-words.jpg'},
    {'id': 5, 'title': 'Great Expectations', 'author': 'Charles Dickens', 'genre': 'Classic', 'price': '7.99', 'cover': 'https://i.postimg.cc/y6MSZGmp/great-expectations.jpg'},
    {'id': 6, 'title': 'War and Peace', 'author': 'Leo Tolstoy', 'genre': 'Historical Fiction', 'price': '20.99', 'cover': 'https://i.postimg.cc/wBjtzYzM/war-and-peace.jpg'},
    {'id': 7, 'title': 'Gulliver’s Travels', 'author': 'Jonathan Swift', 'genre': 'Satire', 'price': '11.99', 'cover': 'https://i.postimg.cc/3NvYhnWd/gulliver-s-travels.jpg'},
    {'id': 9, 'title': 'Invisible Man', 'author': 'Ralph Ellison', 'genre': 'Fiction', 'price': '14.99', 'cover': 'https://i.postimg.cc/43ffc62S/invisible-man.jpg'},
    {'id': 10, 'title': 'King Lear', 'author': 'William Shakespeare', 'genre': 'Tragedy', 'price': '9.99', 'cover': 'https://i.postimg.cc/LX72Gr9c/king-lear.jpg'},
    {'id': 11, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Classic', 'price': '12.99', 'cover': 'https://i.postimg.cc/Hs1Vxymf/pride-and-prejudice.jpg'},
]

def get_book_details(book_id):
    # Convert book_id to an integer for a consistent comparison
    book_id = int(book_id)
    # Find the book in the book_catalog using the book_id
    book = next((book for book in book_catalog if book['id'] == book_id), None)
    return book


@app.route('/')
def index():
    return render_template('index.html', books=book_catalog, current_user=current_user)


# Home route
#@app.route('/')
#def index():
#    return render_template('index.html', books=book_catalog)

# Search route
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = [book for book in book_catalog if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
    return render_template('search.html', query=query, results=results)

# Add to cart route
# Add to cart route
@app.route('/add_to_cart/<int:book_id>')
def add_to_cart(book_id):
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    book_id_str = str(book_id)  # Convert book ID to string
    cart[book_id_str] = cart.get(book_id_str, 0) + 1  # Use string keys
    session['cart'] = cart
    session.modified = True
    
    # Redirect to the referrer page; if it's None, redirect to index
    return redirect(request.referrer or url_for('index'))

#Remove from cart route
@app.route('/remove_from_cart/<int:book_id>')
def remove_from_cart(book_id):
    cart = session.get('cart', {})
    cart.pop(str(book_id), None)  # Use string keys
    session['cart'] = cart
    session.modified = True
    return redirect(url_for('show_cart'))

@app.route('/remove_one_from_cart/<int:book_id>')
def remove_one_from_cart(book_id):
    cart = session.get('cart', {})
    book_id_str = str(book_id)  # Convert book ID to string
    if cart.get(book_id_str, 0) > 1:
        cart[book_id_str] -= 1
    else:
        cart.pop(book_id_str, None)
    session['cart'] = cart
    session.modified = True
    return redirect(url_for('show_cart'))

# Show cart route
@app.route('/cart')
def show_cart():
    cart_book_ids = session.get('cart', {})
    cart_books = {book_id: {'details': get_book_details(book_id), 'quantity': quantity}
                  for book_id, quantity in cart_book_ids.items()}
    return render_template('cart.html', cart=cart_books)


# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        existing_user = User.query.filter_by(email=email).first()
        if existing_user is None:
            new_user = User(email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Email already exists.', 'error')
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.', 'info')
    return redirect(url_for('index'))


# Purchase route
@app.route('/purchase', methods=['POST'])
@login_required
def purchase():
    # Implement purchase functionality here
    flash('Purchase complete!')
    session.pop('cart', None)  # Clear the cart
    return redirect(url_for('index'))

@app.route('/checkout')
@login_required  # Assuming the user must be logged in to checkout
def checkout():
    # You can include any other information needed for the checkout process here
    return render_template('checkout.html')

@app.route('/process_payment', methods=['POST'])
@login_required
def process_payment():
    payment_method = request.form.get('payment_method')

    # You would have your payment processing logic here
    # For now, we'll assume the payment is always successful

    # Clear the cart here since payment is successful
    session.pop('cart', None)

    # Instead of redirecting immediately, render the payment_success template
    return render_template('payment_success.html')


    # If payment is successful:
    flash('Payment successful!', 'success')
    # Clear the cart here if payment is successful
    session.pop('cart', None)
    # Redirect to a confirmation page or back to the cart
    return redirect(url_for('index'))  # Change 'index' to your confirmation route if you have one


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

