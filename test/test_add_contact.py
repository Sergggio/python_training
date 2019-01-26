# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", home_phone="",
                    mobile_phone="", work_phone="", secondary_phone="", email="")] + \
           [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), home_phone=random_string("homephone", 10),
            mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
            secondary_phone=random_string("secondary_phone", 10), email=random_string("email", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
     old_contacts = app.contact.get_contact_list()
     app.contact.create(contact)
     new_contacts = app.contact.get_contact_list()
     print(new_contacts)
     assert len(old_contacts) + 1 == app.contact.count()
     old_contacts.append(contact)
     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
