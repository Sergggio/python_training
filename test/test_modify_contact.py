# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="temporary_contact1", lastname="temporary_contact1", address="Moscow", home_phone="1234567", email="123@test.ru"))
    app.contact.edit(Contact(firstname="Name2", lastname="LastName2", address="Omsk", home_phone="654321", email="321@test.ru"))
