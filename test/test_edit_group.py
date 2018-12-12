# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="test_edited", header="header_edited", footer="comment_edited"))
    app.session.logout()
