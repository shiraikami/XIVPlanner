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

    gearsets = db.relationship('GearSet', cascade="all,delete", backref="users")
    acquiredgear = db.relationship('AcquiredGear', cascade="all,delete", backref="users")

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

    @classmethod
    def update(cls, username, password, user_id):
        """Updates the user with new username and/or password."""

        user = cls.query.get(user_id)

        if user:
            if password != '':
                hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')
                user.password = hashed_pwd
            if username != '':
                user.username = username
            else:
                user.username = user.username

            db.session.add(user)
            return user

        return False


class Character(db.Model):
    """User's character data from FFXIV."""

    __tablename__ = 'characters'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    character_id = db.Column(
        db.Integer
    )

    name = db.Column(
        db.Text
    )

    portrait = db.Column(
        db.Text
    )

    lodestone_id = db.Column(
        db.Integer
    )

    __table_args__ = (
        db.UniqueConstraint('user_id', 'character_id', name='user_character'), 
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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }


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

    classjob = db.Column(
        db.Text
    )

    equipslot = db.Column(
        db.Integer
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "url": self.url,
            "ilevel": self.ilevel,
            "classjob": self.classjob,
            "equipslot": self.equipslot
        }

class GearSet(db.Model):
    """List of gear the user saved."""

    __tablename__ = 'gearsets'

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

    name = db.Column(
        db.Text
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

    lring_id = db.Column(
        db.Integer,
        db.ForeignKey('rings.id')
    )

    rring_id = db.Column(
        db.Integer,
        db.ForeignKey('rings.id')
    )

    acquiredgear = db.relationship('AcquiredGear', cascade="all,delete", backref="gearsets")

class AcquiredGear(db.Model):
    """Piece of gear each user has."""

    __tablename__ = 'acquiredgear'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    gearset_id = db.Column(
        db.Integer,
        db.ForeignKey('gearsets.id')
    )

    gear_id = db.Column(
        db.Integer
    )
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'gear_id', name='acquired_unique'),
    )

    def to_dict(self):
        """Serialize data to a dict of specific gear info."""

        return {
            "gear_id": self.gear_id,
            "gearset_id": self.gearset_id,
            "user_id": self.user_id
        }

def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)