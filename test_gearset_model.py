"""Gearset model test."""

# run these tests like:
# 
#   python -m unittest test_gearset_model.py

import os
from unittest import TestCase
from models import db, connect_db, User, GearSet, Weapon, Offhand, Helmet, Body, Gloves, Pants, Boots, Earring, Necklace, Bracelet, Ring

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ.get('DATABASE_URL', 'postgresql:///xivplanner_test')

from app import app

class GearSetModelTestCase(TestCase):
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

            weapon = Weapon(name="test")
            weapon.id = 1
            offhand = Offhand(name="test")
            offhand.id = 1
            helmet = Helmet(name="test")
            helmet.id = 1
            body = Body(name="test")
            body.id = 1
            gloves = Gloves(name="test")
            gloves.id = 1
            pants = Pants(name="test")
            pants.id = 1
            boots = Boots(name="test")
            boots.id = 1
            earring = Earring(name="test")
            earring.id = 1
            necklace = Necklace(name="test")
            necklace.id = 1
            bracelet = Bracelet(name="test")
            bracelet.id = 1
            ring = Ring(name="test")
            ring.id = 1

            db.session.add_all([weapon, offhand, helmet, body, gloves, pants, boots, earring, necklace, bracelet, ring])
            db.session.commit()

            u1 = User.query.get(uid1)

            self.u1 = u1
            self.uid1 = uid1
        
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_gearset_model(self):
        """Basic model."""

        g = GearSet(user_id=self.uid1, 
                    job="Job", 
                    name="TEST",
                    weapon_id=1,
                    offhand_id=1,
                    helmet_id=1,
                    body_id=1,
                    gloves_id=1,
                    pants_id=1,
                    boots_id=1,
                    earring_id=1,
                    necklace_id=1,
                    bracelet_id=1,
                    lring_id=1,
                    rring_id=1)

        with app.app_context():
            gid = 1111
            g.id = gid
            db.session.add(g)
            db.session.commit()

            g = GearSet.query.get(gid)
            u1 = User.query.get(self.uid1)

            self.assertIsNotNone(g)
            self.assertEqual(g.user_id, self.uid1)
            self.assertEqual(g.job, "Job")
            self.assertEqual(g.name, "TEST")
            self.assertEqual(g.weapon_id, 1)
            self.assertEqual(len(u1.gearsets), 1)