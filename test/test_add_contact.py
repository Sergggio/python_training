# -*- coding: utf-8 -*-
from model.contact import Contact


# data_contacts - to load from contacts.by, json_contacts - to load from contacts.json
def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
