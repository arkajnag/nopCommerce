import sys
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.locators import ObjectRepository as OR
from Pages.eCommerceRegisterPage import RegisterPage
from Utils.webaction_utilities import select_element_by_attribute, click_on_element, send_text_to_element


class LaunchPage:

    def __init__(self, driver):
        self.driver = driver
        self.webDriverWait = WebDriverWait(self.driver, 10)
        self.SELECT_COUNTRY_CURRENCY_BY_ID = self.webDriverWait.until \
            (EC.presence_of_element_located((By.ID, OR.SELECT_COUNTRY_CURRENCY_BY_ID)))
        self.LINK_REGISTER_BY_LINKTEXT = self.webDriverWait.until \
            (EC.presence_of_element_located((By.LINK_TEXT, OR.LINK_REGISTER_BY_LINKTEXT)))
        self.TXT_SEARCH_ITEM_BY_ID = self.webDriverWait.until(EC.presence_of_element_located
                                                              ((By.ID, OR.TXT_SEARCH_ITEM_BY_ID)))
        self.BUTTON_SEARCH_ITEM_BY_CSS = self.webDriverWait.until(EC.presence_of_element_located
                                                                  ((By.CSS_SELECTOR, OR.BUTTON_SEARCH_ITEM_BY_CSS)))

    def fnc_changeCurrenyForShopping(self, currencyFormat):
        try:
            select_element_by_attribute(self.SELECT_COUNTRY_CURRENCY_BY_ID, currencyFormat)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    def fnc_clickOnRegistrationLink(self):
        try:
            click_on_element(self.LINK_REGISTER_BY_LINKTEXT)
            return RegisterPage(self.driver)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    def fnc_search_item_from_launch_page(self, searchItem):
        try:
            send_text_to_element(self.TXT_SEARCH_ITEM_BY_ID, searchItem)
            click_on_element(self.BUTTON_SEARCH_ITEM_BY_CSS)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
