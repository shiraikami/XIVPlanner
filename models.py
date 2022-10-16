"""SQLAlchemy models for XIVPlanner."""

from enum import unique
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    password = db.Column(
        db.Text,
        nullable = False
    )

    statics = db.relationship('Static', secondary="staticmembers", backref="users")
    gearsets = db.relationship('GearSet', backref="users")

    @classmethod
    def signup(cls, username, password):
        """Sign up user.
        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            password=hashed_pwd,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.
        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.
        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


class Static(db.Model):
    """Static/Guild in the system."""

    __tablename__ = 'statics'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )


class StaticMember(db.Model):
    """Static/Guild members in the system."""

    __tablename__ = 'staticmembers'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    static_id = db.Column(
        db.Integer,
        db.ForeignKey('statics.id')
    )


class Weapon(db.Model):
    """Gear list for a user."""

    __tablename__ = 'weapons'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Offhand(db.Model):
    """Gear list for a user."""

    __tablename__ = 'offhands'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Helmet(db.Model):
    """Gear list for a user."""

    __tablename__ = 'helmets'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True        
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Body(db.Model):
    """Gear list for a user."""

    __tablename__ = 'bodies'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Gloves(db.Model):
    """Gear list for a user."""

    __tablename__ = 'gloves'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Pants(db.Model):
    """Gear list for a user."""

    __tablename__ = 'pants'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Boots(db.Model):
    """Gear list for a user."""

    __tablename__ = 'boots'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Earring(db.Model):
    """Gear list for a user."""

    __tablename__ = 'earrings'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Necklace(db.Model):
    """Gear list for a user."""

    __tablename__ = 'necklaces'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Bracelet(db.Model):
    """Gear list for a user."""

    __tablename__ = 'bracelets'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class Ring(db.Model):
    """Gear list for a user."""

    __tablename__ = 'rings'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    icon = db.Column(
        db.Text
    )

    url = db.Column(
        db.Text
    )

    ilevel = db.Column(
        db.Integer
    )

class GearSet(db.Model):
    """List of gear the user saved."""

    __tablename__ = 'gearset'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    job = db.Column(
        db.Text,
        nullable = False
    )

    weapon_id = db.Column(
        db.Integer,
        db.ForeignKey('weapons.id')
    )

    offhand_id = db.Column(
        db.Integer,
        db.ForeignKey('offhands.id')

    )

    helmet_id = db.Column(
        db.Integer,
        db.ForeignKey('helmets.id')
    )

    body_id = db.Column(
        db.Integer,
        db.ForeignKey('bodies.id')
    )

    gloves_id = db.Column(
        db.Integer,
        db.ForeignKey('gloves.id')
    )

    pants_id = db.Column(
        db.Integer,
        db.ForeignKey('pants.id')
    )

    boots_id = db.Column(
        db.Integer,
        db.ForeignKey('boots.id')
    )

    earring_id = db.Column(
        db.Integer,
        db.ForeignKey('earrings.id')
    )

    necklace_id = db.Column(
        db.Integer,
        db.ForeignKey('necklaces.id')
    )

    bracelet_id = db.Column(
        db.Integer,
        db.ForeignKey('bracelets.id')
    )

    ring1_id = db.Column(
        db.Integer,
        db.ForeignKey('rings.id')
    )

    ring2_id = db.Column(
        db.Integer,
        db.ForeignKey('rings.id')
    )

def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)