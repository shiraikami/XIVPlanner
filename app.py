"""XIVPlanner Flask app."""

from email import generator
import os
from flask import Flask, render_template, request, redirect, session, flash, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
import requests

from forms import UserSignUpForm, LoginForm, UserEditForm
from models import db, connect_db, User, Weapon, Offhand, Helmet, Body, Gloves, Pants, Boots, Earring, Necklace, Bracelet, Ring, GearSet

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
            return render_template('/users/signup.html', form=form)

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

    return render_template('/users/login.html', form=form)


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
    return render_template('/users/profile.html', user=user)


@app.route("/profile/id/<int:user_id>/edit", methods=["GET", "POST"])
def edit_profile(user_id):
    """Shows the edit page for a user."""

    user = User.query.get(user_id)
    form = UserEditForm()

    if form.validate_on_submit():
        try:
            if(User.authenticate(g.user.username, form.confirmpass.data)):
                User.update(form.username.data, form.password.data, user.id)
                db.session.commit()

        except IntegrityError:    
            flash("Username already taken", 'error')
            return render_template('/profile/id/' + str(g.user.id), form=form)

        return redirect("/profile/id/" + str(g.user.id))

    else:
        return render_template('/users/profile_edit.html', form=form)


@app.route("/profile/id/<int:user_id>/delete", methods=["GET"])
def delete_profile(user_id):
    """Deletes the user."""

    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")



##############################################################################
# Gear routes

@app.route("/gear")
def show_gear():
    """Show the gear page of a user."""

    return render_template('gear/gear_create.html')


@app.route("/gear/save", methods=["POST"])
def save_gear():
    """Save the current gearset of user."""

    job = request.form.get('job')
    name = request.form.get('name')
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


@app.route("/gear/id/<int:gearset_id>")
def gear_detail(gearset_id):
    """Shows a gearset that is saved."""
    
    gearset = GearSet.query.get(gearset_id)
    weapon = Weapon.query.get(gearset.weapon_id)
    offhand = Offhand.query.get(gearset.offhand_id)
    helmet = Helmet.query.get(gearset.helmet_id)
    body = Body.query.get(gearset.body_id)
    gloves = Gloves.query.get(gearset.gloves_id)
    pants = Pants.query.get(gearset.pants_id)
    boots = Boots.query.get(gearset.boots_id)
    earring = Earring.query.get(gearset.earring_id)
    necklace = Necklace.query.get(gearset.necklace_id)
    bracelet = Bracelet.query.get(gearset.bracelet_id)
    lring = Ring.query.get(gearset.lring_id)
    rring = Ring.query.get(gearset.rring_id)

    return render_template("/gear/gear_detail.html", gearset=gearset, weapon=weapon, offhand=offhand, helmet=helmet, body=body, gloves=gloves, pants=pants, boots=boots, earring=earring, necklace=necklace, bracelet=bracelet, lring=lring, rring=rring)


@app.route("/gear/id/<int:gearset_id>/edit")
def gear_show_edit(gearset_id):
    """Shows a page for user to edit a gearset."""

    gearset = GearSet.query.get(gearset_id)
    weapon = Weapon.query.get(gearset.weapon_id)
    offhand = Offhand.query.get(gearset.offhand_id)
    helmet = Helmet.query.get(gearset.helmet_id)
    body = Body.query.get(gearset.body_id)
    gloves = Gloves.query.get(gearset.gloves_id)
    pants = Pants.query.get(gearset.pants_id)
    boots = Boots.query.get(gearset.boots_id)
    earring = Earring.query.get(gearset.earring_id)
    necklace = Necklace.query.get(gearset.necklace_id)
    bracelet = Bracelet.query.get(gearset.bracelet_id)
    lring = Ring.query.get(gearset.lring_id)
    rring = Ring.query.get(gearset.rring_id)
    return render_template('gear/gear_edit.html', gearset=gearset, weapon=weapon, offhand=offhand, helmet=helmet, body=body, gloves=gloves, pants=pants, boots=boots, earring=earring, necklace=necklace, bracelet=bracelet, lring=lring, rring=rring)


@app.route("/gear/id/<int:gearset_id>/edit", methods=["POST"])
def gear_save_edit(gearset_id):
    """Shows a page for user to edit a gearset."""
    print(request.form.get('job'))

    editgearset = GearSet.query.get(gearset_id)
    if request.form.get('job') == None:
        editgearset.job = editgearset.job
    else:
        editgearset.job = request.form.get('job')

    if request.form.get('weapon') == None:
        editgearset.weapon_id = editgearset.weapon_id
    else:
        editgearset.weapon_id = request.form.get('weapon')


    if request.form.get('offhand') == None:
        editgearset.offhand_id = editgearset.offhand_id
    else:
        editgearset.offhand_id = request.form.get('offhand')

    if request.form.get('helmet') == None:
        editgearset.helmet_id = editgearset.helmet_id
    else:
        editgearset.helmet_id = request.form.get('helmet')

    if request.form.get('body') == None:
        editgearset.body_id = editgearset.body_id
    else:
        editgearset.body_id = request.form.get('body')

    if request.form.get('gloves') == None:
        editgearset.gloves_id = editgearset.gloves_id
    else:
        editgearset.gloves_id = request.form.get('gloves')

    if request.form.get('pants') == None:
        editgearset.pants_id = editgearset.pants_id
    else:
        editgearset.pants_id = request.form.get('pants')

    if request.form.get('boots') == None:
        editgearset.boots_id = editgearset.boots_id
    else:
        editgearset.boots_id = request.form.get('boots')

    if request.form.get('earring') == None:
        editgearset.earring_id = editgearset.earring_id
    else:
        editgearset.earring_id = request.form.get('earring')

    if request.form.get('necklace') == None:
        editgearset.necklace_id = editgearset.necklace_id
    else:
        editgearset.necklace_id = request.form.get('necklace')

    if request.form.get('bracelet') == None:
        editgearset.bracelet_id = editgearset.bracelet_id
    else:
        editgearset.bracelet_id = request.form.get('bracelet')

    if request.form.get('lring') == None:
        editgearset.lring_id = editgearset.lring_id
    else:
        editgearset.lring_id = request.form.get('lring')

    if request.form.get('rring') == None:
        editgearset.rring_id = editgearset.rring_id
    else:
        editgearset.rring_id = request.form.get('rring')
        
    editgearset.name = request.form.get('name')
    
    db.session.add(editgearset)
    db.session.commit()
    return redirect("/gear/id/" + str(gearset_id))


@app.route("/gear/id/<int:gearset_id>/delete", methods=["POST"])
def gear_delete(gearset_id):
    """Deletes a gearset."""

    gearset = GearSet.query.get(gearset_id)
    db.session.delete(gearset)
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
# Homepage

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template('home.html')