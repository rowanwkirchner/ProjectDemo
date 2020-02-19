from select import select

from selenium.webdriver.common.by import By
from toolium.pageelements import *
from toolium.pageobjects.page_object import PageObject


class CreateAccountPageObject(PageObject):
    """Class represents mobile page elements for Login page."""

    mr_radio_btn = None
    mrs_radio_btn = None
    firstname = None
    lastname = None
    email = None
    password = None
    address_firstname = None
    address_lastname = None
    address_company = None
    address = None
    address_line2 = None
    address_city = None
    address_state = None
    address_zip = None
    address_country = None
    address_mobile_number = None
    address_used = None
    parent_element = None
    button_select = None
    button_select_state = None
    register_button = None

    def init_page_elements(self):
        """Initialize mobile page elements using element locator."""

        self.mrs_radio_btn = Button(By.ID, 'uniform-id_gender2')
        self.firstname = Text(By.ID, 'customer_firstname')
        self.lastname = Text(By.ID, 'customer_lastname')
        self.email = Text(By.ID, 'email')
        self.password = Text(By.ID, 'passwd')

        self.address_firstname = Text(By.ID, 'firstname', wait=False)
        self.address_lastname = Text(By.ID, 'lastname', wait=False)
        self.address_company = Text(By.ID, 'company', wait=False)

        self.address = Text(By.ID, 'address1', wait=False)
        self.address_line2 = Text(By.ID, 'address2', wait=False)
        self.address_city = Text(By.ID, 'city', wait=False)

        self.button_select = Button(By.ID, 'uniform-id_state', wait=True)
        self.address_state = Button(By.ID, 'id_state', parent=self.button_select_state)
        # self.button_select_state = Button(By.TAG_NAME, 'option', wait=False,)

        self.address_zip = Text(By.ID, 'postcode', wait=False)
        self.address_country = Button(By.ID, 'uniform-id_country', wait=False)

        self.address_mobile_number = Text(By.ID, 'phone', wait=False)
        self.address_used = Text(By.ID, 'alias', wait=False)
        self.register_button = Button(By.ID, 'submitAccount', wait=False)

