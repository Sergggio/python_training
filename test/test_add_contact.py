# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Name1", lastname="LastName1", address="Moscow", home_phone="1234567", email="123@test.ru"))
