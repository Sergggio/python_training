# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.choose()
    app.contact.delete()
    app.session.logout()

