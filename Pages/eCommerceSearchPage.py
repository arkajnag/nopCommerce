from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
