# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Name1", lastname="LastName1", address="Moscow", home_phone="1234567", email="123@test.ru"))
    app.session.logout()
