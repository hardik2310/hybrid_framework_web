import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from assignment_without_POM.utilities.read_utils import get_csv_as_list
from with_POM_exercise.config.conftest import WebDriverWrapper


class TestInvalidLogin(WebDriverWrapper):

    @pytest.mark.parametrize("name, mobile_number, password, expected_error",
                             get_csv_as_list(file_path='../test_data/test_invalid_create_user_data.csv'))
    def test_invalid_login(self, name, mobile_number, password, expected_error):
        """To verify the create user with invalid data"""

        self.wait = WebDriverWait(self.driver, 10)
        action = webdriver.ActionChains(self.driver)

        action.move_to_element(self.driver.find_element(By.ID, "nav-link-accountList")).perform()
        self.driver.find_element(By.LINK_TEXT, 'Start here.').click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Create Account']")))

        self.driver.find_element(By.ID, "ap_customer_name").send_keys(name)
        if str(mobile_number) != 'nan':
            Select(self.driver.find_element(By.ID, "auth-country-picker")).select_by_visible_text('IN +91')
            self.driver.find_element(By.ID, "ap_phone_number").send_keys(mobile_number)
        if str(password) != 'nan':
            self.driver.find_element(By.NAME, "password").send_keys(password)

        self.driver.find_element(By.ID, "continue").click()
        actual_error = None
        if str(mobile_number) == 'nan':
            actual_error = self.driver.find_element(By.XPATH,
                                                    "//div[@id='auth-phoneNumber-missing-alert']//div[@class='a-alert-content']").text
        if str(password) == 'nan':
            actual_error = self.driver.find_element(By.XPATH,
                                                    "//div[@id='auth-password-missing-alert']//div[@class='a-alert-content']").text

        assert_that(expected_error).is_equal_to(actual_error)
