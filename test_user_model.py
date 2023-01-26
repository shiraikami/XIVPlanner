"""User model test."""

# run these tests like:
# 
#   python -m unittest test_user_model.py

import os
from unittest import TestCase
from sqlalchemy import exc
from models import db, connect_db, User

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ.get('DATABASE_URL', 'postgresql:///xivplanner_test')

from app import app

class UserModelTestCase(TestCase):
    """Test user model."""

    def setUp(self):
        """Create test client, add sample data."""
        self.app = app
        with self.app.app_context():
            db.drop_all()
            db.create_all()

            u1 = User.signup("test1", "password")
            uid1 = 1111
            u1.id = uid1

            db.session.commit()

            u1 = User.query.get(uid1)

            self.u1 = u1
            self.uid1 = uid1
        
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_user_model(self):
        """Basic model."""

        u = User(username="test", password="password")

        with app.app_context():
            db.session.add(u)
            db.session.commit()

            # User should have no gearsets, acquiredgear, characters linked or following characters
            self.assertEqual(len(u.gearsets), 0)
            self.assertEqual(len(u.acquiredgear), 0)
            self.assertEqual(len(u.characters), 0)
            self.assertEqual(len(u.following), 0)

    ####
    #
    # Signup Tests
    #
    ####
    def test_valid_signup(self):
        with app.app_context():
            u_test = User.signup("validsignup", "password")
            uid = 3333
            u_test.id = uid
            db.session.commit()

            u_test = User.query.get(uid)
            self.assertIsNotNone(u_test)
            self.assertEqual(u_test.username, "validsignup")
            # Bcrypt strings should start with $2b$
            self.assertTrue(u_test.password, "$2b$")

    def test_invalid_username_signup(self):
        with app.app_context():
            invalid = User.signup(None, "password")
            uid = 3333
            invalid.id = uid
            with self.assertRaises(exc.IntegrityError) as context:
                db.session.commit()

    def test_invalid_password_signup(self):
        with app.app_context():
            with self.assertRaises(ValueError) as context:
                User.signup("invalid", None)
            
            with self.assertRaises(ValueError) as context:
                User.signup("invalid", "")

    ####
    #
    # Authentication Tests
    #
    ####
    def test_valid_authentication(self):
        with app.app_context():
            u = User.authenticate(self.u1.username, "password")
            self.assertIsNotNone(u)
            self.assertEqual(u.id, self.uid1)

    def test_invalid_username(self):
        with app.app_context():
            self.assertFalse(User.authenticate("badusername", "password"))

    def test_wrong_password(self):
        with app.app_context():
            self.assertFalse(User.authenticate(self.u1.username, "badpassword"))