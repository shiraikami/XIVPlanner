"""XIVPlanner Flask app."""

from email import generator
import os
from flask import Flask, render_template, request, redirect, session, flash, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import requests

from forms import UserSignUpForm, LoginForm
from models import db, connect_db, User, Weapon, Offhand, Helmet, Body, Gloves, Pants, Boots, Earring, Necklace, Bracelet, Ring, GearSet, Static, StaticMember

CURR_USER = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///XIVPlanner'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'SECRET')
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

##############################################################################
# Gear routes

@app.route("/gear")
def show_gear():
    """Show the gear page of a user."""

    return render_template('gear/gear.html')


@app.route("/gear/save", methods=["POST"])
def save_gear():
    """Save the current gearset of user."""

    job = request.form.get('job')
    name = request.form.get('setname')
    weapon = request.form.get('weapon')
    offhand = request.form.get('offhand')
    helmet = request.form.get('helmet')
    body = request.form.get('body')
    gloves = request.form.get('gloves')
    pants = request.form.get('pants')
    boots = request.form.get('boots')
    earring = request.form.get('earring')
    necklace = request.form.get('necklace')
    bracelet = request.form.get('bracelet')
    lring = request.form.get('lring')
    rring = request.form.get('rring')

    gearset = GearSet(user_id=g.user.id, job=job, name=name, weapon_id=weapon, offhand_id=offhand, helmet_id=helmet, body_id=body, gloves_id=gloves, pants_id=pants, boots_id=boots, earring_id=earring, necklace_id=necklace, bracelet_id=bracelet, lring_id=lring, rring_id=rring)
    db.session.add(gearset)
    db.session.commit()
    return redirect("/gear")


@app.route("/api/gear")
def api_gear():
    """Sends necessary gear data as JSON."""

    gears = []
    weapons = db.session.query(Weapon).filter(or_(Weapon.name.contains("Abyssos"),Weapon.name.contains("Augmented Lunar Envoy")))
    offhands = db.session.query(Offhand).filter(or_(Offhand.name.contains("Abyssos"),Offhand.name.contains("Augmented Lunar Envoy")))
    helmet = db.session.query(Helmet).filter(or_(Helmet.name.contains("Abyssos"),Helmet.name.contains("Augmented Lunar Envoy")))
    body = db.session.query(Body).filter(or_(Body.name.contains("Abyssos"),Body.name.contains("Augmented Lunar Envoy")))
    gloves = db.session.query(Gloves).filter(or_(Gloves.name.contains("Abyssos"),Gloves.name.contains("Augmented Lunar Envoy")))
    pants = db.session.query(Pants).filter(or_(Pants.name.contains("Abyssos"),Pants.name.contains("Augmented Lunar Envoy")))
    boots = db.session.query(Boots).filter(or_(Boots.name.contains("Abyssos"),Boots.name.contains("Augmented Lunar Envoy")))
    earrings = db.session.query(Earring).filter(or_(Earring.name.contains("Abyssos"),Earring.name.contains("Augmented Lunar Envoy")))
    necklaces = db.session.query(Necklace).filter(or_(Necklace.name.contains("Abyssos"),Necklace.name.contains("Augmented Lunar Envoy")))
    bracelets = db.session.query(Bracelet).filter(or_(Bracelet.name.contains("Abyssos"),Bracelet.name.contains("Augmented Lunar Envoy")))
    rings = db.session.query(Ring).filter(or_(Ring.name.contains("Abyssos"),Ring.name.contains("Augmented Lunar Envoy")))
    gears.extend(weapons)
    gears.extend(offhands)
    gears.extend(helmet)
    gears.extend(body)
    gears.extend(gloves)
    gears.extend(pants)
    gears.extend(boots)
    gears.extend(earrings)
    gears.extend(necklaces)
    gears.extend(bracelets)
    gears.extend(rings)
    gears = [gear.to_dict() for gear in gears]

    return jsonify(gears)


@app.route("/fflogs")
def show_fflogs():
    """Show the FFLogs page."""

    return render_template('users/fflogs.html')

##############################################################################
# Static routes

@app.route("/static")
def create_static():
    """Show the static/guild page."""

    dc = requests.get("https://xivapi.com/servers/dc").json()
    print(g.user.statics)
    return render_template('static/create.html', dc=dc)


@app.route("/static/id/<int:static_id>")
def show_static(static_id):
    """Show details about a specific static."""

    static = Static.query.get(static_id)
    return render_template('static/details.html', static=static)


@app.route("/static/save", methods=["POST"])
def save_static():
    """Save the static/guild created by user."""

    name = request.form.get('name')
    faction = request.form.get('faction')
    server = request.form.get('server')
    static = Static(name=name, faction=faction, server=server)
    db.session.add(static)
    db.session.commit()
    staticmember = StaticMember(role="Leader", username=g.user.username, user_id=g.user.id, static_id=static.id)
    db.session.add(staticmember)
    db.session.commit()
    return redirect("/")

##############################################################################
# Homepage

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template('home.html')