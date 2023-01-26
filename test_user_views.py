"""User views test."""

# run these tests like:
# 
#   python -m unittest test_user_views.py

import os
from unittest import TestCase
from models import db, User

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

    def test_show_signup(self):
        with self.client as c:
            resp = c.get("/signup")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<h2 class="join-message">Sign up for XIVPlanner</h2>""", str(resp.data))

    def test_post_signup(self):
        with self.client as c:
           
            resp = c.post("/signup", data={"username": "testsignup", "password": "password"})
                
            self.assertEqual(resp.status_code, 302)

            u = User.query.get(1)
            self.assertEqual(u.username, "testsignup")

    def test_login_show(self):
        with self.client as c:
            resp = c.get("/login")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<h2 class="join-message">Welcome back.</h2>""", str(resp.data))

    def test_login_post(self):
        with self.client as c:
            resp = c.post("/login", data={"username": self.testuser.username, "password": "password"})

            self.assertEqual(resp.status_code, 302)

    def test_login_post_invalid(self):
        with self.client as c:
            resp = c.post("/login", data={"username": "invalid", "password": "invalid"})

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""Invalid credentials.""", str(resp.data))

    def test_edit_view(self):
        with self.client as c:
            with c.session_transaction() as sess:
                    sess[CURR_USER] = self.testuser.id

            resp = c.get(f"/user/id/{self.testuser.id}/edit")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<form method="POST" id="user_form">""", str(resp.data))

    def test_edit_view_invalid_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                    sess[CURR_USER] = 12412254

            resp = c.get(f"/user/id/{self.testuser.id}/edit", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized", str(resp.data))

    def test_edit_view_no_session(self):
        with self.client as c:

            resp = c.get(f"/user/id/{self.testuser.id}/edit", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized", str(resp.data))

    def test_edit_post(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id

            resp = c.post(f"/user/id/{self.testuser.id}/edit", data={"username": "editeduser", "password": "password", "confirmpass": "password"})

            editeduser = User.query.get(self.testuser_id)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(editeduser.username, "editeduser")
    
    def test_edit_post_taken(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id

            resp = c.post(f"/user/id/{self.testuser.id}/edit", 
                                data={"username": "testuser2", "password": "password", "confirmpass": "password"},
                                follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Username already taken", str(resp.data))

    def test_edit_post_invalid(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id

            resp = c.post(f"/user/id/{self.testuser.id}/edit", 
                                data={"username": "editeduser", "password": "password", "confirmpass": "invalid"}, 
                                follow_redirects=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Wrong Password.", str(resp.data))

    def test_delete(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id

            resp = c.post(f"/user/id/{self.testuser.id}/delete", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<p class="m-3">Welcome to XIVPlanner!""", str(resp.data))

    def test_delete_no_session(self):
        with self.client as c:
            
            resp = c.post(f"/user/id/{self.testuser.id}/delete", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))

    def test_delete_invalid_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = 12342352

            resp = c.post(f"/user/id/{self.testuser.id}/delete", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))