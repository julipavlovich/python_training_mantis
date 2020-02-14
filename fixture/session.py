class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd  # извлекли ссылку на драйвер
        self.app.open_home_page()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='navbar-container']/div[2]/ul/li[3]/a/i[2]").click()
        wd.find_element_by_link_text("Logout").click()
        # wd.implicitly_wait(3)
        # wd.find_element_by_name("user")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                #  вышли из метода
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("a.dropdown-toggle span.user-info").text
