# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    contact = Contact(firstname="temporary_contact1", lastname="temporary_contact1")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.choose()
    app.contact.delete()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

