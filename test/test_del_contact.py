# -*- coding: utf-8 -*-

from model.contact import Contact
import random


def test_delete_random_contact(app, db, check_ui):
    contact = Contact(firstname="Name2", lastname="LastName2")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    contact_to_delete = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact_to_delete.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_to_delete)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
