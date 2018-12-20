# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="temporary_contact1", lastname="temporary_contact1"))
    app.contact.choose()
    app.contact.delete()
