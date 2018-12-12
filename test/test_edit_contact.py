# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="Name2", lastname="LastName2", address="Omsk", home_phone="654321", email="321@test.ru"))
    app.session.logout()
