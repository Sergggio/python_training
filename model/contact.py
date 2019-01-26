from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, address=None, all_phones_from_home_page=None,
                home_phone=None, work_phone=None, mobile_phone=None, secondary_phone=None, email=None,
                email2=None, email3=None, all_email_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.secondary_phone = secondary_phone
        self.all_email_from_home_page = all_email_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
