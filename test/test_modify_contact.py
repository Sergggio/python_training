# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="temporary_contact1", lastname="temporary_contact1"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="Name2", lastname="LastName2")
    contact_for_edit = random.choice(old_contacts)
    id = contact_for_edit.id
    contact.id = id
    app.contact.modify_contact_by_id(contact_for_edit.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for i in range(len(old_contacts)):
        if old_contacts[i].id == contact_for_edit.id:
            old_contacts[i] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
