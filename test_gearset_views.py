"""Gear views test."""

# run these tests like:
# 
#   python -m unittest test_user_views.py

import os
from unittest import TestCase
import json
from models import db, User, GearSet, AcquiredGear, Weapon, Offhand, Helmet, Body, Gloves, Pants, Boots, Earring, Necklace, Bracelet, Ring

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ.get('DATABASE_URL', 'postgresql:///xivplanner_test')

from app import app, CURR_USER

with app.app_context():
    db.drop_all()

app.config['WTF_CSRF_ENABLED'] = False

class GearSetViewsTestCase(TestCase):
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

            weapon = Weapon(name="test", icon="")
            weapon.id = 1
            offhand = Offhand(name="test", icon="")
            offhand.id = 1
            helmet = Helmet(name="test", icon="")
            helmet.id = 1
            body = Body(name="test", icon="")
            body.id = 1
            gloves = Gloves(name="test", icon="")
            gloves.id = 1
            pants = Pants(name="test", icon="")
            pants.id = 1
            boots = Boots(name="test", icon="")
            boots.id = 1
            earring = Earring(name="test", icon="")
            earring.id = 1
            necklace = Necklace(name="test", icon="")
            necklace.id = 1
            bracelet = Bracelet(name="test", icon="")
            bracelet.id = 1
            ring = Ring(name="test", icon="")
            ring.id = 1

            gearset = GearSet(user_id=testuser_id, 
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
            
            gearset_id = 1111
            gearset.id = gearset_id

            db.session.add_all([weapon, offhand, helmet, body, gloves, pants, boots, earring, necklace, bracelet, ring, gearset])
            db.session.commit()

            testuser = User.query.get(testuser_id)
            testuser2 = User.query.get(testuser2_id)
            gearset = GearSet.query.get(gearset_id)

            self.testuser = testuser
            self.testuser_id = testuser_id
            self.testuser2 = testuser2
            self.testuser2_id = testuser2_id
            self.gearset = gearset
            self.gearset_id = gearset_id

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_gearset_show(self):
        with self.client as c:
            resp = c.get("/gearset")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<form action="/gearset/save" method="POST" style="margin-top: 70px;">""", str(resp.data))

    def test_gearset_post(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id

            resp = c.post("/gearset/save", data={"job": "job",
                                            "name": "testview",
                                            "weapon": 1,
                                            "offhand": 1,
                                            "helmet": 1,
                                            "body": 1,
                                            "gloves": 1,
                                            "pants": 1,
                                            "boots": 1,
                                            "earring": 1,
                                            "necklace": 1,
                                            "bracelet": 1,
                                            "lring": 1,
                                            "rring": 1})

            gearset = GearSet.query.get(1)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(gearset.job, "job")
            self.assertEqual(gearset.name, "testview")
            self.assertEqual(gearset.weapon_id, 1)

    def test_gearset_post_no_session(self):
        with self.client as c:
            
            resp = c.post("/gearset/save", data={}, follow_redirects=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))

    def test_gearset_post_invalid_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = 123425251
            
        resp = c.post("/gearset/save", data={}, follow_redirects=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("Access unauthorized.", str(resp.data))

    def test_gearset_delete(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id

            resp = c.post(f"/gearset/id/{self.gearset.id}/delete", follow_redirects=True)

            deleted = GearSet.query.get(self.gearset_id)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<form action="/gearset/save" method="POST" style="margin-top: 70px;">""", str(resp.data))
            self.assertEqual(deleted, None)

    def test_gearset_delete_no_session(self):
        with self.client as c:

            resp = c.post(f"/gearset/id/{self.gearset.id}/delete", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))

    def test_gearset_delete_invalid_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = 12252161

            resp = c.post(f"/gearset/id/{self.gearset.id}/delete", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized.", str(resp.data))

    def test_gearset_acquired(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER] = self.testuser.id

            resp = c.post(f"/gearset/id/{self.gearset_id}", data=json.dumps(dict(checked=True, gear=1)), content_type='application/json')

            gear = AcquiredGear.query.filter_by(gear_id=1).first()

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(gear.user_id, self.testuser.id)
            self.assertEqual(gear.gear_id, 1)