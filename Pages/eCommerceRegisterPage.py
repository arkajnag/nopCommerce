import sys
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.locators import ObjectRepository as OR
from Utils.webaction_utilities import click_on_element, send_text_to_element, select_element_by_attribute


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.genders = self.driver.find_elements(By.CSS_SELECTOR, OR.RADIO_GENDERS_BY_CSS)
        self.firstname = self.wait.until(EC.presence_of_element_located((By.ID, OR.TXT_FIRSTNAME_BY_ID)))
        self.lastname = self.wait.until(EC.presence_of_element_located((By.ID, OR.TXT_LASTNAME_BY_ID)))
        self.email = self.wait.until(EC.presence_of_element_located((By.ID, OR.TXT_EMAIL_BY_ID)))
        self.password = self.wait.until(EC.presence_of_element_located((By.ID, OR.TXT_PASSWORD_BY_ID)))
        self.confirm_password = self.wait.until(EC.presence_of_element_located((By.ID, OR.TXT_CONFIRM_PASSWORD_BY_ID)))
        self.newsletter_checkbox = self.wait.until(
            EC.presence_of_element_located((By.ID, OR.CHECKBOX_NEWSLETTER_BY_ID)))
        self.day = self.wait.until(EC.presence_of_element_located((By.NAME, OR.SELECT_DAY_BY_NAME)))
        self.month = self.wait.until(EC.presence_of_element_located((By.NAME, OR.SELECT_MONTH_BY_NAME)))
        self.year = self.wait.until(EC.presence_of_element_located((By.NAME, OR.SELECT_YEAR_BY_NAME)))
        self.register_button = self.wait.until(EC.presence_of_element_located((By.ID, OR.BUTTON_REGISTER_BY_ID)))

    def fnc_enter_new_registration_details(self, gender, fname, lname, email, dob, password):
        try:
            for eachVal in self.genders:
                if eachVal.text == gender:
                    click_on_element(eachVal)
                    break
            send_text_to_element(self.firstname, fname)
            send_text_to_element(self.lastname, lname)
            send_text_to_element(self.email, email)
            day, month, year = str(dob).split("-")
            select_element_by_attribute(self.day, day)
            select_element_by_attribute(self.month, month)
            select_element_by_attribute(self.year, year)
            if self.newsletter_checkbox.is_selected():
                click_on_element(self.newsletter_checkbox)
            send_text_to_element(self.password, password)
            send_text_to_element(self.confirm_password, password)
            click_on_element(self.register_button)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    def fnc_verify_registration_completion_message(self):
        try:
            if self.wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, OR.LABEL_REGISTRATION_SUCCESS_BY_CSS))):
                success_message = self.wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, OR.LABEL_REGISTRATION_SUCCESS_BY_CSS))).text
                click_on_element(self.wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, OR.BUTTON_REGISTER_CONTINUE_BY_CSS))))
                return success_message
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
