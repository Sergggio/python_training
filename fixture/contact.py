

class ContactHelper():


    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_xpath("(//input[@value='Enter'])").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
