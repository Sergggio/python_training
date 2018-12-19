# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="temporary_contact1", lastname="temporary_contact1", address="Moscow", home_phone="1234567", email="123@test.ru"))
    app.contact.choose()
    app.contact.delete()
