"""User model test."""

# run these tests like:
# 
#   python -m unittest test_user_model.py

import os
from unittest import TestCase
from sqlalchemy import exc
from models import db, User, Character, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///xivplanner_test"

# Import app

from app import app

# Create our tables 

with app.app_context():
    db.create_all()

class UserModelTestCase(TestCase):
    """Test user model."""

    def setUp(self):
        """Create test client, add sample data."""
        with app.app_context():
            db.drop_all()
            db.create_all()

            u1 = User.signup("test1", "password")
            u1id = 1
            u1.id = u1id

            u2 = User.signup("test2", "password")
            u2id = 2
            u2.id = u2id

            db.session.commit()

            u1 = User.query.get(u1id)
            u2 = User.query.get(u2id)

        self.u1 = u1
        self.u1id = u1id

        self.u2 = u2
        self.u2id = u2id

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        with app.app_context():
            db.session.rollback()
        return res

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

    