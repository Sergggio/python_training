import re
from model.contact import Contact


def test_all_contacts(app, db):
    contacts_from_db = db.get_contact_list()
    phone_list_from_db = db.phones_from_db()
    #email_liset_from_db = db.emails_from_db()
    phone_list = []
    for phone in phone_list_from_db:
        phone_list.append(merge_phones_like_on_home_page(phone))
    email_list = []
    #for email in email_liset_from_db:
    #    email_list.append(merge_mail_like_on_home_page(email))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    phones_from_home_page = [con.all_phones_from_home_page for con in contacts_from_home_page]
    #emails_from_home_page = [con.all_mail_from_home_page for con in contacts_from_home_page]
    assert phone_list == phones_from_home_page
    #assert email_list == emails_from_home_page
    assert contacts_from_db == contacts_from_home_page


def clear(s):
    return re.sub("[() -]", "", s)


def remove_spaces(s):
    return re.sub(' +', ' ', s).rstrip()


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone,
                                        contact.work_phone, contact.secondary_phone]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: remove_spaces(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
