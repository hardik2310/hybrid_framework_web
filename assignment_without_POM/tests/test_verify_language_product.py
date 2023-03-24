import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from assignment_without_POM.utilities.read_utils import get_excel_as_list
from with_POM_exercise.config.conftest import WebDriverWrapper


class TestLanguageBook(WebDriverWrapper):
    @pytest.mark.parametrize("first_language, second_language, item_name, book_name, search_result",
                             get_excel_as_list(io='../test_data/item_data.xlsx',
                                               sheet_name='test_language_book'))
    def test_verify_language_book(self, first_language, second_language, item_name, book_name, search_result):
        self.wait = WebDriverWait(self.driver, 10)
        action = webdriver.ActionChains(self.driver)

        """select language using mouse over and click"""
        action.move_to_element(self.driver.find_element(By.ID, "icp-nav-flyout")).perform()
        self.driver.find_element(By.XPATH, '//div[@id="nav-flyout-icp"]//span[text()="' + first_language + '"]').click()
        language_value = self.driver.find_element(By.XPATH,
                                                  '//a[@id="icp-nav-flyout"]//div[contains(text(), "HI")]').text
        assert_that(language_value).is_equal_to('HI')

        """select language using mouse over and click"""
        action.move_to_element(self.driver.find_element(By.ID, "icp-nav-flyout")).perform()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
                                                                                     '//div[@id="nav-flyout-icp"]//span[text()="' + second_language + '"]'))
        language_value = self.driver.find_element(By.XPATH,
                                                  '//a[@id="icp-nav-flyout"]//div[contains(text(), "EN")]').text
        assert_that(language_value).is_equal_to('EN')

        """select values dropdown"""
        self.drop_down_object = self.wait.until(ec.presence_of_element_located((By.ID, "searchDropdownBox")))
        Select(self.drop_down_object).select_by_visible_text(item_name)
        search_box_dropdown_value = Select(self.drop_down_object).first_selected_option.text
        assert_that(search_box_dropdown_value).is_equal_to(item_name)

        """search book"""
        self.driver.find_element(By.ID, 'twotabsearchtextbox').clear()
        self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(book_name)
        self.driver.find_element(By.ID, 'nav-search-submit-button').send_keys(Keys.ENTER)
        search_box_input_value = self.driver.find_element(By.ID, 'twotabsearchtextbox').get_attribute('value')
        assert_that(search_box_input_value).is_equal_to(book_name)

        element_found = self.driver.find_element(By.XPATH, '//span[text()="' + search_result + '"]').is_displayed()
        assert element_found == True
