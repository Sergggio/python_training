# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="temporary_contact1", lastname="temporary_contact1"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New_contact_edited", lastname="temporary_contact_edited")
    contact.cont_id = old_contacts[0].cont_id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=id) == sorted(new_contacts, key=id)
