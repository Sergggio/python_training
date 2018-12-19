# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="temporary_group", header="header", footer="comment"))
    app.group.modify_first_group(Group(name="test_edited"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="temporary_group", header="header", footer="comment"))
    app.group.modify_first_group(Group(header="header_edited"))
