"""User views test."""

# run these tests like:
# 
#   python -m unittest test_user_views.py

import os
from unittest import TestCase
from sqlalchemy import exc
from models import db, connect_db, User

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

            self.testuser = User.signup(username="testuser", password="password")
            
            self.testuser_id = 1111
            self.testuser.id = self.testuser_id

            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test__show_signup(self):
        with self.client as c:
            resp = c.get("/signup")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<h2 class="join-message">Sign up for XIVPlanner</h2>""", str(resp.data))

    def test_post_signup(self):
        with self.client as c:
            with c.session_transaction() as sess:
                    sess[CURR_USER] = self.testuser_id
                    resp = c.post("/signup", data={"username": "testsignup", "password": "password"})
                
                    self.assertEqual(resp.status_code, 302)

                    u = User.query.one()
                    self.assertEqual(u.username, "testsignup")