import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    """Show portfolio of stocks"""
    query_cash = db.execute('SELECT cash FROM users WHERE id = ?', session["user_id"])
    if request.method == 'GET':
        query = db.execute('SELECT * FROM wallet WHERE user_id = ?', session["user_id"])
        return render_template('index.html', query=query, lookup=lookup, query_cash=query_cash)
    else:
        old_cash = float(request.form.get('cash'))
        try:
            add_cash = float(request.form.get('addcash'))
        except ValueError:
            return apology('please enter a valid number')
        if add_cash <= 0:
            return apology('invalid amount')
        new_cash = old_cash + add_cash
        db.execute('UPDATE users SET cash = ? WHERE id = ?', new_cash, session["user_id"])
        return redirect('/')

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get('symbol')
        try:
            shares = int(request.form.get('shares'))
        except ValueError:
            return apology("shares is not integer")
        else:
            if shares < 1:
                return apology("shares is negative integer")
        values = lookup(symbol)
        if symbol == '' or values == None:
            return apology("symbol invalid")

        price = values['price']
        total = round(int(shares) * price, 2)
        cash = db.execute('SELECT cash FROM users WHERE id = ?', session["user_id"])
        cash = cash[0]['cash']
        if cash > total:
            new_cash = cash - total
            db.execute('UPDATE users SET cash = ? WHERE id = ?', new_cash, session["user_id"])
            db.execute('INSERT INTO purchases (user_id, price, symbol, shares, type) VALUES (?,?,?,?,"buy")', session["user_id"], price, symbol, shares)

            query_wallet = db.execute('SELECT shares FROM wallet WHERE (user_id,stock) = (?,?)', session["user_id"], symbol)
            if query_wallet:
                new_shares = shares + query_wallet[0]['shares']
                db.execute('UPDATE wallet SET shares = ? WHERE (user_id,stock) = (?,?)', new_shares, session["user_id"], symbol)
            else:
                db.execute('INSERT INTO wallet (user_id, stock, shares) VALUES (?,?,?)', session["user_id"], symbol, shares)

            return redirect("/")
        else:
            return apology("not enough cash")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    query = db.execute('SELECT * FROM purchases')
    return render_template("history.html", query=query)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get('symbol')
        values = lookup(symbol)
        if values == None:
            return apology("invalid symbol", 400)
        return render_template("quoted.html", values=values)
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get('username')
        users = db.execute('SELECT username FROM users')
        if username == '' or username in (rjecnik['username'] for rjecnik in users):
            return apology("must provide username", 400)

        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        if password == '' or password != confirmation:
            return apology("must provide password or passwords dont match", 400)

        hashed = generate_password_hash(request.form.get('password'))
        db.execute('INSERT INTO users (username, hash) VALUES (?, ?)', username, hashed)
        return redirect('/login')
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        symbol = request.form.get('symbol')
        shares = int(request.form.get('shares'))

        values = lookup(symbol)
        if symbol == '' or values == None:
            return apology("symbol invalid")
        price = values['price']

        query_cash = db.execute('SELECT cash FROM users WHERE id = ?', session["user_id"])
        query_wallet = db.execute('SELECT shares FROM wallet WHERE (user_id,stock) = (?,?)', session["user_id"], symbol)

        if query_wallet:
            new_shares = query_wallet[0]['shares'] - shares
            if new_shares < 0:
                return apology('imas premalo dionica')
            new_cash = query_cash[0]['cash'] + (price * shares)
            db.execute('UPDATE wallet SET shares = ? WHERE (user_id,stock) = (?,?)', new_shares, session["user_id"], symbol)
            db.execute('UPDATE users SET cash = ? WHERE id = ?', new_cash, session["user_id"])
            db.execute('INSERT INTO purchases (user_id, price, symbol, shares, type) VALUES (?,?,?,?,"sell")', session["user_id"], price, symbol, shares)

            return redirect('/')
        else:
            return apology('nemas te dionice')

    else:
        symbols = db.execute('SELECT stock FROM wallet WHERE user_id = ?', session["user_id"])
        return render_template('sell.html', symbols=symbols)
