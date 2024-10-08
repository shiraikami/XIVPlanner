from app import app, db
from models import Weapon, Offhand, Helmet, Body, Gloves, Pants, Boots, Earring, Necklace, Bracelet, Ring
import requests

with app.app_context():
    db.drop_all()
    db.create_all() 

try:
    print("**********************************************")
    print("Requesting weapon data from XIVAPI...")
    weapon_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=1&page={page}").json()
        new_response = response.get('Results', [])
        weapon_data.extend(new_response)
        page += 1

    for weapon in weapon_data:
        weap = Weapon(id=weapon['ID'], name=weapon['Name'], icon=weapon['Icon'], url=weapon['Url'], ilevel=weapon['LevelItem'], classjob=weapon['ClassJobCategory']['Name'], equipslot=weapon['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(weap)
            db.session.commit()
except:
    print("API request error with 'weapon data'")


try:
    print("**********************************************")
    print("Requesting weapon data from XIVAPI...")
    weapon_data2 = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=13&page={page}").json()
        new_response = response.get('Results', [])
        weapon_data2.extend(new_response)
        page += 1
        
    for weapon in weapon_data2:
        weap = Weapon(id=weapon['ID'], name=weapon['Name'], icon=weapon['Icon'], url=weapon['Url'], ilevel=weapon['LevelItem'], classjob=weapon['ClassJobCategory']['Name'], equipslot=weapon['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(weap)
            db.session.commit()
except:
    print("API request error with 'weapon data'")


try:
    print("**********************************************")
    print("Requesting offhand data from XIVAPI...")
    offhand_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=2&page={page}").json()
        new_response = response.get('Results', [])
        offhand_data.extend(new_response)
        page += 1

    for offhand in offhand_data:
        off = Offhand(id=offhand['ID'], name=offhand['Name'], icon=offhand['Icon'], url=offhand['Url'], ilevel=offhand['LevelItem'], classjob=offhand['ClassJobCategory']['Name'], equipslot=offhand['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(off)
            db.session.commit()
except:
    print("API request error with 'offhand data'")


try:
    print("**********************************************")
    print("Requesting helmet data from XIVAPI...")
    helmet_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=3&page={page}").json()
        new_response = response.get('Results', [])
        helmet_data.extend(new_response)
        page += 1

    for helmet in helmet_data:
        hel = Helmet(id=helmet['ID'], name=helmet['Name'], icon=helmet['Icon'], url=helmet['Url'], ilevel=helmet['LevelItem'], classjob=helmet['ClassJobCategory']['Name'], equipslot=helmet['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(hel)
            db.session.commit()
except:
    print("API request error with 'helmet data'")


try:
    print("**********************************************")
    print("Requesting body data from XIVAPI...")
    body_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=4&page={page}").json()
        new_response = response.get('Results', [])
        body_data.extend(new_response)
        page += 1

    for body in body_data:
        bod = Body(id=body['ID'], name=body['Name'], icon=body['Icon'], url=body['Url'], ilevel=body['LevelItem'], classjob=body['ClassJobCategory']['Name'], equipslot=body['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(bod)
            db.session.commit()
except:
    print("API request error with 'body data'")


try:
    print("**********************************************")
    print("Requesting gloves data from XIVAPI...")
    gloves_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=5&page={page}").json()
        new_response = response.get('Results', [])
        gloves_data.extend(new_response)
        page += 1

    for gloves in gloves_data:
        glove = Gloves(id=gloves['ID'], name=gloves['Name'], icon=gloves['Icon'], url=gloves['Url'], ilevel=gloves['LevelItem'], classjob=gloves['ClassJobCategory']['Name'], equipslot=gloves['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(glove)
            db.session.commit()
except:
    print("API request error with 'gloves data'")


try:
    print("**********************************************")
    print("Requesting pants data from XIVAPI...")
    pants_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=7&page={page}").json()
        new_response = response.get('Results', [])
        pants_data.extend(new_response)
        page += 1

    for pants in pants_data:
        pant = Pants(id=pants['ID'], name=pants['Name'], icon=pants['Icon'], url=pants['Url'], ilevel=pants['LevelItem'], classjob=pants['ClassJobCategory']['Name'], equipslot=pants['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(pant)
            db.session.commit()
except:
    print("API request error with 'pants data'")


try:
    print("**********************************************")
    print("Requesting boots data from XIVAPI...")
    boots_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=8&page={page}").json()
        new_response = response.get('Results', [])
        boots_data.extend(new_response)
        page += 1

    for boots in boots_data:
        boot = Boots(id=boots['ID'], name=boots['Name'], icon=boots['Icon'], url=boots['Url'], ilevel=boots['LevelItem'], classjob=boots['ClassJobCategory']['Name'], equipslot=boots['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(boot)
            db.session.commit()
except:
    print("API request error with 'boots data'")


try:
    print("**********************************************")
    print("Requesting earring data from XIVAPI...")
    earring_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=9&page={page}").json()
        new_response = response.get('Results', [])
        earring_data.extend(new_response)
        page += 1

    for earring in earring_data:
        ear = Earring(id=earring['ID'], name=earring['Name'], icon=earring['Icon'], url=earring['Url'], ilevel=earring['LevelItem'], classjob=earring['ClassJobCategory']['Name'], equipslot=earring['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(ear)
            db.session.commit()
except:
    print("API request error with 'earring data'")


try:
    print("**********************************************")
    print("Requesting necklace data from XIVAPI...")
    necklace_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=10&page={page}").json()
        new_response = response.get('Results', [])
        necklace_data.extend(new_response)
        page += 1

    for necklace in necklace_data:
        neck = Necklace(id=necklace['ID'], name=necklace['Name'], icon=necklace['Icon'], url=necklace['Url'], ilevel=necklace['LevelItem'], classjob=necklace['ClassJobCategory']['Name'], equipslot=necklace['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(neck)
            db.session.commit()
except:
    print("API request error with 'necklace data'")


try:
    print("**********************************************")
    print("Requesting bracelet data from XIVAPI...")
    bracelet_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=11&page={page}").json()
        new_response = response.get('Results', [])
        bracelet_data.extend(new_response)
        page += 1
    
    for bracelet in bracelet_data:
        brace = Bracelet(id=bracelet['ID'], name=bracelet['Name'], icon=bracelet['Icon'], url=bracelet['Url'], ilevel=bracelet['LevelItem'], classjob=bracelet['ClassJobCategory']['Name'], equipslot=bracelet['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(brace)
            db.session.commit()
except:
    print("API request error with 'bracelet data'")


try:
    print("**********************************************")
    print("Requesting ring data from XIVAPI...")
    ring_data = []
    new_response = True
    page = 1
    while new_response:
        response = requests.get(f"https://xivapi.com/search?columns=ID,Name,Icon,Url,LevelItem,ClassJobCategory,EquipSlotCategory.ID&filters=EquipSlotCategory.ID=12&page={page}").json()
        new_response = response.get('Results', [])
        ring_data.extend(new_response)
        page += 1

    for ring in ring_data:
        r = Ring(id=ring['ID'], name=ring['Name'], icon=ring['Icon'], url=ring['Url'], ilevel=ring['LevelItem'], classjob=ring['ClassJobCategory']['Name'], equipslot=ring['EquipSlotCategory']['ID'])
        with app.app_context():
            db.session.add(r)
            db.session.commit()
except:
    print("API request error with 'ring data'")

print("**********************************")
print("Added all gear to database...")