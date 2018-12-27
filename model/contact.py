from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home_phone=None, email=None, cont_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_phone = home_phone
        self.email = email
        self.cont_id = cont_id

    def __repr__(self):
        return "%s:%s" % (self.cont_id, self.lastname)

    def __eq__(self, other):
        return (self.cont_id is None or other.cont_id is None or self.cont_id == other.cont_id) and self.lastname == other.lastname

    def id_or_max(self):
        if self.cont_id:
            return int(self.cont_id)
        else:
            return maxsize
