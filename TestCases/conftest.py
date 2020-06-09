import os
from selenium import webdriver
import pytest
import datetime
import sys
import traceback

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Utils.common_utilities import parseConfigurationFile


@pytest.fixture()
def initialize(request):
    try:
        print(f"\nTest started at {datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M')}")
        driver = webdriver.Firefox(executable_path=parseConfigurationFile()['FIREFOX_EXE_PATH'])
        driver.maximize_window()
        driver.set_page_load_timeout(10)
        driver.delete_all_cookies()
        driver.implicitly_wait(20)
        driver.get(parseConfigurationFile()['BASE_URL'])
        request.cls.driver = driver
        yield driver
        if driver is not None:
            driver.quit()
        print(f"\nTest ended at {datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M')}")
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)
