import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.eCommerceLaunchPage import LaunchPage
from Utils.common_utilities import parseConfigurationFile, randomNumber, current_timestamp


@pytest.mark.usefixtures('initialize')
class Test_RegistrationPage:

    @pytest.mark.parametrize("gender,fname,lname,email,dob,passowrd", [
        ('Male', 'Arka', 'Nag', 'arkajnag3@gmail.com', '15-January-1956', '1qazxcvbnm')
    ])
    def test_verify_customer_registration(self, gender, fname, lname, email, dob, passowrd):
        driver = self.driver
        launch_page = LaunchPage(driver)
        register_page = launch_page.fnc_clickOnRegistrationLink()
        email = str(randomNumber(10, 999)) + email
        register_page.fnc_enter_new_registration_details(gender, fname, lname, email, dob, passowrd)
        driver.save_screenshot("./Screenshots/Registration"+current_timestamp('%d%m%y%H%M')+".png")
        registration_complete_msg = register_page.fnc_verify_registration_completion_message()
        assert registration_complete_msg == parseConfigurationFile()['REGISTRATION_SUCCESS_MESSAGE']
