import sys
import traceback

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as Action


def send_text_to_element(element, text_to_input):
    try:
        element.send_keys(text_to_input)
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


def click_on_element(element):
    try:
        element.click()
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


def select_element_by_attribute(element, attributeValue):
    try:
        if type(attributeValue) == int:
            Select(element).select_by_index(attributeValue)
        elif type(attributeValue) == str:
            Select(element).select_by_visible_text(attributeValue)
        else:
            Select(element).select_by_value(attributeValue)
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


def move_to_element(element, driver):
    try:
        Action(driver).move_to_element(element).perform()
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


def move_to_element_by_offset(element, xOffset, yOffset, driver):
    try:
        Action(driver).move_to_element_with_offset(element, xOffset, yOffset).perform()
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


def move_to_element_and_Click(element, driver):
    try:
        Action(driver).move_to_element(element).click().perform()
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)

