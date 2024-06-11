from seleniumbase import BaseCase


class LoginRent(BaseCase):
    def test_login_rent(self):
        # open page
        self.open("http://localhost:3000/")

        # click login
        self.click("#menu-icon-hamburger")
        self.click("#login-button")
        self.sleep(1)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/Login")

        self.sleep(1)

        # login
        self.send_keys('#username', 'tyler')
        # self.sleep(1)
        self.send_keys('#password', 'strongPassword')
        self.sleep(1)
        self.click("#log-in-button")
        self.sleep(2)

        # check to see if we are on home url logged in
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/")

        self.get("http://localhost:3000/profile")

        # self.sleep(1)
        self.find_element('h1:contains("Test Create Form")').click()
        self.sleep(1)
        self.click("#return-tool")
        self.sleep(1)
        self.click("#confirm-return")
        # fill form
        # self.send_keys("#search", "Test Create Form")
        # self.sleep(1)
        #
        # # hit enter
        # self.click("#enter")
        # self.sleep(1)
        #
        # # check to see if we are on search page
        # get_started_url = self.get_current_url()
        # self.assert_equal(get_started_url, "http://localhost:3000/search")
        #
        # # click listing button
        # # self.sleep(1)
        # self.find_element('h1:contains("Test Create Form")').click()
        #
        # # check to see if we are on new listing url logged in
        # get_started_url = self.get_current_url()
        # self.assert_equal(get_started_url, "http://localhost:3000/listing")
        #
        # # enter start date
        # self.sleep(1)
        # self.send_keys("#mui-10", "05/31/2023")
        #
        # # enter end date
        # self.sleep(1)
        # self.send_keys("#mui-11", "06/10/2023")
        #
        # # select rate
        # # self.sleep(1)
        # # self.send_keys("#demo-simple-select", "06/10/2023")
        # # self.sleep(1)
        # # self.select_option_by_value('#demo-simple-select', '80')
        # # self.sleep(1)
        # self.click("#rent-now")
        #
        # self.sleep(1)
        # # check to see if we are on home url with listing gone
        # get_started_url = self.get_current_url()
        # self.assert_equal(get_started_url, "http://localhost:3000/checkout")
        #
        # self.click("checkout-now")
        #
        self.sleep(3)
