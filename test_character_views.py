"""Character views test."""

# run these tests like:
# 
#   python -m unittest test_user_views.py

import os
from unittest import TestCase
from models import db, User, Character, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ.get('DATABASE_URL', 'postgresql:///xivplanner_test')

from app import app, CURR_USER

with app.app_context():
    db.drop_all()

app.config['WTF_CSRF_ENABLED'] = False

class CharacterViewsTestCase(TestCase):
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

            character = Character(name="name", server="server", user_id=testuser_id, character_id=1, portrait="portrait")
            character_id = 1111
            character.id = character_id

            follow = Follows(char_being_followed_id=1, 
                             char_being_followed_name="name", 
                             char_being_followed_server="server", 
                             char_being_followed_portrait="portrait",
                             user_following_id=testuser_id)
            follow_id = (1,testuser_id)

            db.session.add_all([character, follow])
            db.session.commit()

            testuser = User.query.get(testuser_id)
            testuser2 = User.query.get(testuser2_id)
            character = Character.query.get(1111)
            follow = Follows.query.get(follow_id)

            self.testuser = testuser
            self.testuser_id = testuser_id
            self.testuser2 = testuser2
            self.testuser2_id = testuser2_id
            self.character = character
            self.character_id = character_id
            self.follow = follow
            self.follow_id = follow_id

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_character_search(self):
        with self.client as c:

            resp = c.get("/search", data={"term": ""})

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Characters", str(resp.data))

    def test_character_searched(self):
        with self.client as c:

            resp = c.get(f"/character/id/{32328486}")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<p hidden id="char-id">""", str(resp.data))

    def test_character_link(self):
        with self.client as c:
            with c.session_transaction() as sess:
                    sess[CURR_USER] = self.testuser.id

            resp = c.post(f"/character/id/{32328486}/link", data={})

            character = Character.query.filter_by(character_id=32328486).first()    
            user = User.query.get(self.testuser.id)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(character.user_id, self.testuser.id)
            self.assertEqual(character.character_id, 32328486)
            self.assertEqual(len(user.characters), 2)

    def test_character_link_no_session(self):
        with self.client as c:

            resp = c.post(f"/character/id/{32328486}/link", data={}, follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))

    def test_character_unlink(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id
            
            resp = c.post(f"/character/id/{1}/unlink")

            user = User.query.get(self.testuser.id)
            character = Character.query.filter_by(character_id=1).first()

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(len(user.characters), 0)
            self.assertEqual(character, None)
            
    def test_character_unlink_no_session(self):
        with self.client as c:

            resp = c.post(f"/character/id/{1}/unlink", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))

    def test_character_unlink_invalid_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = 1234252

            resp = c.post(f"/character/id/{1}/unlink", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))

    def test_character_follow(self):
        with self.client as c:
            with c.session_transaction() as sess:
                    sess[CURR_USER] = self.testuser.id

            resp = c.post(f"/character/id/{32328486}/follow", data={})

            follow = Follows.query.get((32328486, self.testuser.id))
            user = User.query.get(self.testuser.id)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(follow.user_following_id, self.testuser.id)
            self.assertEqual(follow.char_being_followed_id, 32328486)
            self.assertEqual(len(user.following), 2)

    def test_character_follow_no_session(self):
        with self.client as c:

            resp = c.post(f"/character/id/{32328486}/follow", data={}, follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))   

    def test_character_unfollow(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id
            
            resp = c.post(f"/character/id/{1}/unfollow")

            follow = Follows.query.get((32328486, self.testuser.id))
            user = User.query.get(self.testuser.id)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(len(user.following), 0)
            self.assertEqual(follow, None)
            
    def test_character_unfollow_no_session(self):
        with self.client as c:

            resp = c.post(f"/character/id/{1}/unfollow", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))

    def test_character_unfollow_invalid_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = 1234252

            resp = c.post(f"/character/id/{1}/unfollow", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))