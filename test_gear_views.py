"""Gear views test."""

# run these tests like:
# 
#   python -m unittest test_user_views.py

import os
from unittest import TestCase
from models import db, User, Gear

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ.get('DATABASE_URL', 'postgresql:///xivplanner_test')

from app import app, CURR_USER

with app.app_context():
    db.drop_all()

app.config['WTF_CSRF_ENABLED'] = False

class UserViewsTestCase(TestCase):
    """Test user views."""

    def setUp(self):
        """Create test client, add sample data."""
        app.testing = True
        self.app = app
        with self.app.app_context():
            db.drop_all()
            db.create_all()

            self.client = app.test_client()

            testuser = User.signup(username="testuser", password="password")
            testuser_id = 1111
            testuser.id = testuser_id

            testuser2 = User.signup(username="testuser2", password="password")
            testuser2_id = 2222
            testuser2.id = testuser2_id

            db.session.commit()

            testuser = User.query.get(testuser_id)
            testuser2 = User.query.get(testuser2_id)

            self.testuser = testuser
            self.testuser_id = testuser_id
            self.testuser2 = testuser2
            self.testuser2_id = testuser2_id

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()