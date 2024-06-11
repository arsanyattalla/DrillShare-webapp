from seleniumbase import BaseCase
from datetime import date, timedelta


class LoginRent(BaseCase):
    def test_login_rent(self):
        # open page
        self.open("http://localhost:3000/")

        # click login
        self.click("#menu-icon-hamburger")
        self.click("#login-button")
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/Login")

        self.sleep(1)

        # login
        self.send_keys('#username', 'tyler')
        # self.sleep(1)
        self.send_keys('#password', 'strongPassword')
        # self.sleep(1)
        self.click("#log-in-button")
        self.sleep(3)

        # check to see if we are on home url logged in
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/")

        # fill form
        self.send_keys("#search-bar", "Test Create Form")
        self.sleep(2)

        # hit enter
        self.click("#hit-enter")
        self.sleep(2)

        # check to see if we are on search page
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/search")

        # click listing button
        # self.sleep(1)
        self.find_element('h5:contains("Test Create Form")').click()

        # check to see if we are on new listing url logged in
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/listing")

        # enter start date
        self.sleep(1)
        rentDateStart = date.today().strftime("%m/%d/%Y")
        rentDateEnd = (date.today() + timedelta(3)).strftime("%m/%d/%Y")
        self.send_keys("#mui-22", rentDateStart)

        # enter end date
        self.sleep(1)

        self.send_keys("#mui-23", rentDateEnd)

        # select rate
        # self.sleep(1)
        # self.send_keys("#demo-simple-select", "06/10/2023")
        # self.sleep(1)
        # self.select_option_by_value('#demo-simple-select', '80')
        # self.sleep(1)
        self.click("#rent-now")

        self.sleep(2)
        # check to see if we are on home url with listing gone
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/checkout")
        self.sleep(1)

        self.click("#checkout-button")

        self.sleep(3)
