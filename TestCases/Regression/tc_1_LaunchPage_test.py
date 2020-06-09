import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.eCommerceLaunchPage import LaunchPage
from Utils.common_utilities import parseConfigurationFile


@pytest.mark.usefixtures("initialize")
class Test_LaunchPage:

    @pytest.mark.parametrize("currenyOption", ['Euro'])
    def test_verify_currency_option_change(self, currenyOption):
        driver = self.driver
        launch_page = LaunchPage(driver)
        launch_page.fnc_changeCurrenyForShopping(currenyOption)

    def test_verify_RegisterPage_opens_on_click_RegisterLink(self):
        driver = self.driver
        launch_page = LaunchPage(driver)
        launch_page.fnc_clickOnRegistrationLink()
        assert driver.title == parseConfigurationFile()['REGISTER_PAGE_TITLE']

    @pytest.mark.parametrize("itemname", ['laptop'])
    def test_verify_item_search_from_launch_page(self, itemname):
        driver = self.driver
        launch_page = LaunchPage(driver)
        launch_page.fnc_search_item_from_launch_page(itemname)
        assert driver.title == parseConfigurationFile()['SEARCH_PAGE_TITLE']
