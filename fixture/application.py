from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()  # передали ссылку на драйвер
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd  # извлекли ссылку на драйвер
        if not (wd.current_url.endswith("/login_page.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.get(self.base_url)

    def destroy(self):  # разрушаем фикстуру
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
