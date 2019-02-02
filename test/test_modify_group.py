# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="temporary_group", header="header", footer="comment"))
    old_groups = db.get_group_list()
    group_to_modify = random.choice(old_groups)
    index = old_groups.index(group_to_modify)
    group = Group(name="New_group_edited")
    group.id = group_to_modify.id
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
