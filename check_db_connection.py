import mysql.connector
from fixture.db import DbFixture
from fixture.orm import ORMFixture


#db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#    print("Groups: ")
#    print(len(groups))
#    print("Contacts: ")
#    print(len(contacts))

try:
    l = db.get_contacts_in_group(Group(id="11"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
