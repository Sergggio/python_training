# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Name1", lastname="LastName1",
                      home_phone="1234567", mobile_phone="1234", work_phone="12345", secondary_phone="123456")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
