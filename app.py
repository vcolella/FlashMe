from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology, password_req
from lib import SQL
import os
import datetime
import json

# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///flashMe.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

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
        return redirect("/"), flash(f"Welcome back {rows[0]['username']} !", 200)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    """Homepage"""

    if request.method == "POST":
        return render_template("index.html")

    else:
        return redirect("/list_sets")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted and matches
        if not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide password and confirmation", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password and confirmation must match", 400)

        if not password_req(request.form.get("password")):
            return apology("password doesn't fill requirements", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username=?", request.form.get("username"))

        if len(rows) > 0:
            return apology("username already registered", 400)

        # Since password and username are good, we can insert it to the table
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                   request.form.get("username"), generate_password_hash(request.form.get("password")))
        rows = db.execute("SELECT * FROM users WHERE username=?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/"), flash(f"Welcome {request.form.get('username')}, you're now registered !", 200)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change user password"""

    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        # Ensure password was submitted and matches database
        if not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("current password is wrong", 400)

        # Ensure password was submitted and matches
        if not request.form.get("new_password") or not request.form.get("confirmation"):
            return apology("must provide password and confirmation", 400)

        if request.form.get("new_password") != request.form.get("confirmation"):
            return apology("new password and confirmation must match", 400)

        if not password_req(request.form.get("password")):
            return apology("password doesn't fill requirements", 400)

        # Update database for username password
        db.execute("UPDATE users SET hash=? WHERE id = ?",
                   generate_password_hash(request.form.get("new_password")), session["user_id"])

        flash("Password successfully changed")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("change_password.html")


@app.route("/new_set", methods=["GET", "POST"])
@login_required
def new_set():
    """Create New Set"""

    if request.method == "POST":

        # # Ensure setName is here
        if not request.form.get("setName"):
            return apology("Set name must be filled", 400)

        rows = db.execute("SELECT * FROM sets WHERE username_id=? AND name=?", session["user_id"], request.form.get("setName"))

        # Update database for set
        if len(rows) > 0:
            db.execute("UPDATE sets SET (description=?, tags=?) WHERE username_id=? AND name=?", request.form.get("setDescription"), request.form.get("setTags"), session["user_id"], request.form.get("setName"))

        else:
            db.execute("INSERT INTO sets (username_id, name, description, tags) VALUES (?, ?, ?, ?)", session["user_id"], request.form.get("setName"), request.form.get("setDescription"), request.form.get("setTags"))
        
        flash(f"You've successfully registered created {request.form.get('setName')}.")

        return redirect("/")
        

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("new_set.html")


@app.route("/new_card", methods=["GET", "POST"])
@login_required
def new_card():
    """Add new card"""

    if request.method == "POST":
        
        # Saves new card

        if not request.form.get("setName") or not request.form.get("cardQuestion") or not request.form.get("cardAnswer"):
            return apology("All fields must be filled", 400)
        
        today = datetime.datetime.today()

        setId = db.execute("SELECT id FROM sets WHERE name=?", request.form.get("setName"))[0]["id"]

        db.execute("INSERT INTO cards (username_id, set_id, question, answer, creation_date) VALUES (?, ?, ?, ?, ?)", session["user_id"], setId, request.form.get("cardQuestion"), request.form.get("cardAnswer"), today.isoformat())

        db.execute("UPDATE sets SET total_cards=total_cards+1 WHERE name=?", request.form.get("setName"))

        flash(f"You've successfully created a new card at {today.strftime('%d/%m/%Y')}.")
        return redirect("/")
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        names = db.execute("SELECT name FROM sets")
        return render_template("new_card.html", names=names)

@app.route("/list_sets", methods=["GET", "POST"])
@login_required
def list_sets():
    """List user sets"""

    if request.method == "POST":

        # # Return set of cards in JSON format
        requestData = request.get_json()
        # # Check database for set id
        rows = db.execute("SELECT id FROM sets WHERE name=?", requestData['setName'])
        # # Update database for user's weight
        if len(rows) > 0:
            setId = rows[0]['id']
            cards = db.execute("SELECT * FROM cards WHERE set_id=?", setId)
            if len(cards) > 0:
                return cards, 200
            else:
                resp = [{
                    "message" : "There are no cards for this set yet."
                }]
                return resp, 400
        else:
            return redirect("/")
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        sets = db.execute("SELECT * FROM sets WHERE username_id=?", session["user_id"])

        if len(sets) > 0:
            return render_template("list_sets.html", sets=sets)
            
        return render_template("list_sets.html")