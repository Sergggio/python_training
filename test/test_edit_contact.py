# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit(Contact(firstname="Name2", lastname="LastName2", address="Omsk", home_phone="654321", email="321@test.ru"))
