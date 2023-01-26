"""Character model test."""

# run these tests like:
# 
#   python -m unittest test_character_model.py

import os
from unittest import TestCase
from models import db, User, Character

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ.get('DATABASE_URL', 'postgresql:///xivplanner_test')

from app import app

class CharacterModelTestCase(TestCase):
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

    def test_character_model(self):
        """Basic model."""

        char = Character(name="test", server="server", portrait="portrait", user_id=self.uid1, character_id=1)

        with app.app_context():
            charid = 1111
            char.id = charid
            db.session.add(char)
            db.session.commit()

            char = Character.query.get(charid)
            u1 = User.query.get(self.uid1)

            self.assertIsNotNone(char)
            self.assertEqual(char.id, 1111)
            self.assertEqual(char.name, "test")
            self.assertEqual(char.server, "server")
            self.assertEqual(char.portrait, "portrait")
            self.assertEqual(char.user_id, self.uid1)
            self.assertEqual(char.character_id, 1)
            self.assertEqual(len(u1.characters), 1)