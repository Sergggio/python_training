# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="temporary_contact1", lastname="temporary_contact1"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Name2", lastname="LastName2")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
