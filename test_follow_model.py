"""Follow model test."""

# run these tests like:
# 
#   python -m unittest test_follow_model.py

import os
from unittest import TestCase
from models import db, User, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ.get('DATABASE_URL', 'postgresql:///xivplanner_test')

from app import app

class FollowModelTestCase(TestCase):
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

    def test_follow_model(self):
        """Basic model."""

        follow = Follows(char_being_followed_id=1111, 
                         char_being_followed_name="name", 
                         char_being_followed_server="server", 
                         char_being_followed_portrait="portrait",
                         user_following_id=self.uid1)

        with app.app_context():
            followid = 1111
            db.session.add(follow)
            db.session.commit()

            follow = Follows.query.get((followid,self.uid1))
            u1 = User.query.get(self.uid1)

            self.assertIsNotNone(follow)
            self.assertEqual(follow.char_being_followed_id, 1111)
            self.assertEqual(follow.char_being_followed_name, "name")
            self.assertEqual(follow.char_being_followed_server, "server")
            self.assertEqual(follow.char_being_followed_portrait, "portrait")
            self.assertEqual(follow.user_following_id, self.uid1)
            self.assertEqual(len(u1.following), 1)