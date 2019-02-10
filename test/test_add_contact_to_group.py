from model.group import Group
from model.contact import Contact
import random


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="FirstGroup"))

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="FirstContact"))

    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())

    old_contacts_from_group = db.get_contacts_in_group(group, db)
    app.contact.add_contact_to_group(group.id, contact.id)
    old_contacts_from_group.append(contact)
    new_contacts_from_group = db.get_contacts_in_group(group, db)

    assert sorted(old_contacts_from_group, key=Contact.id_or_max) == sorted(new_contacts_from_group, key=Contact.id_or_max)
