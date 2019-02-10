from model.group import Group
from model.contact import Contact
import random

def test_del_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="FirstGroup"))

    group = random.choice(db.get_group_list())
    contact = None
    if len(db.get_contacts_in_group(group, db)) == 0:
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="FirstContact"))
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(group.id, contact.id)

    if contact is None:
        contact = random.choice(db.get_contacts_in_group(group))

    old_contacts_from_group = db.get_contacts_in_group(group, db)
    app.contact.remove_contact_from_group(group.id, contact.id)
    old_contacts_from_group.remove(contact)
    new_contacts_from_group = db.get_contacts_in_group(group)

    assert sorted(old_contacts_from_group, key=Contact.id_or_max) == sorted(new_contacts_from_group, key=Contact.id_or_max)
