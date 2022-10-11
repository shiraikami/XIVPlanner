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

    static = db.relationship('Static')
    gear = db.relationship('Gear')

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

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade')
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )


class Gear(db.Model):
    """Gear list for a user."""

    __tablename__ = 'gear'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade')
    )

    weapon = db.Column(
        db.Text,
        nullable = False
    )

    offhand = db.Column(
        db.Text,
        nullable = False
    )

    head = db.Column(
        db.Text,
        nullable = False
    )

    body = db.Column(
        db.Text,
        nullable = False
    )

    gloves = db.Column(
        db.Text,
        nullable = False
    )

    pants = db.Column(
        db.Text,
        nullable = False
    )

    boots = db.Column(
        db.Text,
        nullable = False
    )

    earring = db.Column(
        db.Text,
        nullable = False
    )

    necklace = db.Column(
        db.Text,
        nullable = False
    )

    bracelet = db.Column(
        db.Text,
        nullable = False
    )

    ring1 = db.Column(
        db.Text,
        nullable = False
    )

    ring2 = db.Column(
        db.Text,
        nullable = False
    )


def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)