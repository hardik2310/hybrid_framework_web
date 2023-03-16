import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from without_POM.base.webdriver_listner import WebDriverWrapper
from without_POM.utilities import data_source


class TestInvalidLogin(WebDriverWrapper):

    @pytest.mark.parametrize("email, password, cred_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, email, password, cred_error):
        """To verify the Invalid login"""
        self.driver.find_element(By.ID, "nav-hamburger-menu").click()
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "signInSubmit").click()
        actual_error = self.driver.find_element(By.ID,
                                                "auth-error-message-box").text
        assert_that(cred_error).is_equal_to(actual_error)


class TestVerifyPageValues(WebDriverWrapper):
    @pytest.mark.parametrize("title, url, header", data_source.test_verify_header_title_url)
    def test_verify_title_url_header(self, title, url, header):
        """To verify title, url, header of the page"""
        actual_title = self.driver.title
        actual_url = self.driver.current_url
        actual_header = self.driver.find_element(By.ID, 'nav-logo-sprites').get_attribute('aria-label')

        assert_that(title).is_equal_to(actual_title)
        assert_that(url).is_equal_to(actual_url)
        assert_that(header).is_equal_to(actual_header)
