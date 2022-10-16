from app import app
from models import db, Weapon, Offhand, Helmet, Body, Gloves, Pants, Boots, Earring, Necklace, Bracelet, Ring

import requests

weapon_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=1&page={page}").json()
    new_response = response.get('Results', [])
    weapon_data.extend(new_response)
    page += 1

weapon_data2 = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=13&page={page}").json()
    new_response = response.get('Results', [])
    weapon_data2.extend(new_response)
    page += 1

offhand_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=2&page={page}").json()
    new_response = response.get('Results', [])
    offhand_data.extend(new_response)
    page += 1

helmet_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=3&page={page}").json()
    new_response = response.get('Results', [])
    helmet_data.extend(new_response)
    page += 1

body_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=4&page={page}").json()
    new_response = response.get('Results', [])
    body_data.extend(new_response)
    page += 1

gloves_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=5&page={page}").json()
    new_response = response.get('Results', [])
    gloves_data.extend(new_response)
    page += 1

pants_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=7&page={page}").json()
    new_response = response.get('Results', [])
    pants_data.extend(new_response)
    page += 1

boots_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=8&page={page}").json()
    new_response = response.get('Results', [])
    boots_data.extend(new_response)
    page += 1

earring_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=9&page={page}").json()
    new_response = response.get('Results', [])
    earring_data.extend(new_response)
    page += 1

necklace_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=10&page={page}").json()
    new_response = response.get('Results', [])
    necklace_data.extend(new_response)
    page += 1

bracelet_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=11&page={page}").json()
    new_response = response.get('Results', [])
    bracelet_data.extend(new_response)
    page += 1

ring_data = []
new_response = True
page = 1
while new_response:
    response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem&filters=EquipSlotCategory.ID=12&page={page}").json()
    new_response = response.get('Results', [])
    ring_data.extend(new_response)
    page += 1

for weapon in weapon_data:
    weap = Weapon(id=weapon['ID'], name=weapon['Name'], icon=weapon['Icon'], url=weapon['Url'], ilevel=weapon['LevelItem'])
    db.session.add(weap)
db.commit()

for weapon in weapon_data2:
    weap = Weapon(id=weapon['ID'], name=weapon['Name'], icon=weapon['Icon'], url=weapon['Url'], ilevel=weapon['LevelItem'])
    db.session.add(weap)
db.commit()

for offhand in offhand_data:
    off = Offhand(id=offhand['ID'], name=offhand['Name'], icon=offhand['Icon'], url=offhand['Url'], ilevel=offhand['LevelItem'])
    db.session.add(off)
db.commit()

for helmet in helmet_data:
    hel = Helmet(id=helmet['ID'], name=helmet['Name'], icon=helmet['Icon'], url=helmet['Url'], ilevel=helmet['LevelItem'])
    db.session.add(hel)
db.commit()

for body in body_data:
    bod = Body(id=body['ID'], name=body['Name'], icon=body['Icon'], url=body['Url'], ilevel=body['LevelItem'])
    db.session.add(bod)
db.commit()

for gloves in gloves_data:
    glov = Gloves(id=gloves['ID'], name=gloves['Name'], icon=gloves['Icon'], url=gloves['Url'], ilevel=gloves['LevelItem'])
    db.session.add(glov)
db.commit()

for pants in pants_data:
    pant = Pants(id=pants['ID'], name=pants['Name'], icon=pants['Icon'], url=pants['Url'], ilevel=pants['LevelItem'])
    db.session.add(pant)
db.commit()

for boots in boots_data:
    boot = Boots(id=boots['ID'], name=boots['Name'], icon=boots['Icon'], url=boots['Url'], ilevel=boots['LevelItem'])
    db.session.add(boot)
db.commit()

for earring in earring_data:
    ear = Earring(id=earring['ID'], name=earring['Name'], icon=earring['Icon'], url=earring['Url'], ilevel=earring['LevelItem'])
    db.session.add(ear)
db.commit()

for necklace in necklace_data:
    neck = Necklace(id=necklace['ID'], name=necklace['Name'], icon=necklace['Icon'], url=necklace['Url'], ilevel=necklace['LevelItem'])
    db.session.add(neck)
db.commit()

for bracelet in bracelet_data:
    brace = Bracelet(id=bracelet['ID'], name=bracelet['Name'], icon=bracelet['Icon'], url=bracelet['Url'], ilevel=bracelet['LevelItem'])
    db.session.add(brace)
db.commit()

for ring in ring_data:
    r = Ring(id=ring['ID'], name=ring['Name'], icon=ring['Icon'], url=ring['Url'], ilevel=ring['LevelItem'])
    db.session.add(r)
db.commit()