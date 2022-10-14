"""XIVPlanner Flask app."""

from flask import Flask, render_template, redirect, session, flash, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import UserSignUpForm, LoginForm
from models import connect_db, db, User, Static

CURR_USER = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///XIVPlanner"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "password"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)

##############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER in session:
        g.user = User.query.get(session[CURR_USER])
    else:
        g.user = None

def do_login(user):
    """Log in user."""

    session[CURR_USER] = user.id

def do_logout():
    """Logout user."""

    if CURR_USER in session:
        del session[CURR_USER]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create a new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If there already is a user with that username: flash error message and re-present form."""

    form = UserSignUpForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username = form.username.data,
                password = form.password.data
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'error')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('/users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)

        if user:
            do_login(user)
            return redirect("/")

        flash("Invalid credentials.", 'error')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle user logout."""

    do_logout()
    return redirect("/")


##############################################################################
# User routes

@app.route("/profile/id/<int:user_id>")
def show_profile(user_id):
    """Show the profile of a user."""
    user = User.query.get(user_id)
    return render_template('users/profile.html', user=user)

@app.route("/gear")
def show_gear():
    """Show the gear page of a user."""
    return render_template('users/gear.html')

@app.route("/fflogs")
def show_fflogs():
    """Show the FFLogs page."""
    return render_template('users/fflogs.html')

@app.route("/static")
def show_static():
    """Show the static/guild page."""
    return render_template('users/static.html')

##############################################################################
# Homepage

@app.route("/")
def homepage():
    """Show homepage."""

    flash("Hi")
    return render_template('home.html')