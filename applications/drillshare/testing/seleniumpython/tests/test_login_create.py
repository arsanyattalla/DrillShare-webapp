from seleniumbase import BaseCase


class LoginCreate(BaseCase):
    def test_login_create(self):
        # open page
        self.open("http://localhost:3000/")

        # click login
        self.click("#menu-icon-hamburger")
        self.click("#login-button")
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url,"http://localhost:3000/Login")

        self.sleep(1)

        # login
        self.send_keys('#username', 'kevink')
        self.sleep(1)
        self.send_keys('#password', 'drillshare777')
        self.sleep(1)
        self.click("#log-in-button")
        self.sleep(2)

        # check to see if we are on home url logged in
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/")

        # click burger icon
        self.sleep(1)
        self.click("#burger-button")

        # click create button
        self.sleep(1)
        self.click("#create-button")

        # check to see if we are on create url logged in
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/Create")

        # fill form
        self.send_keys("#tool-name-input-field","Awesome Tool")
        self.send_keys("#tool-category-input-field", "Handheld")
        self.send_keys("#tool-model-number-input-field", "A1235GG")
        self.send_keys("#tool-title-input-field", "Test Create Form")
        self.send_keys("#tool-description-input-field", "Used cement mixer. Little scratches and scuffs but works in"
                                                        " perfect condition! Book Now!")
#         self.send_keys("#tool-hourly-rate-input-field", "20")
        self.send_keys("#tool-daily-rate-input-field", "80")

        # get file path
        self.sleep(1)
        file_path = '../data/mini-cement-mixer.jpg'

        # upload file
        self.sleep(2)
        self.choose_file("#image", file_path)

        # click submit button
        self.sleep(4)
        self.click("#create-new-listing-button")

        self.sleep(3)

        # check to see if we are on home url with new tool posted
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/")

        self.sleep(3)
