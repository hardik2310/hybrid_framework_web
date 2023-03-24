import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from assignment_without_POM.base.webdriver_listner import WebDriverWrapper
from assignment_without_POM.utilities.read_utils import get_excel_as_list


class TestLanguageBook(WebDriverWrapper):
    @pytest.mark.parametrize("item_name, book_name, search_result, quantity",
                             get_excel_as_list(io='../test_data/item_data.xlsx',
                                               sheet_name='book_data'))
    def test_verify_language_book(self, item_name, book_name, search_result, quantity):
        """Verify add item to cart and it's price"""

        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=25)
        action = webdriver.ActionChains(self.driver)

        """select values dropdown"""
        self.drop_down_object = self.wait.until(ec.presence_of_element_located((By.ID, "searchDropdownBox")))
        action.move_to_element(self.drop_down_object).click()
        Select(self.drop_down_object).select_by_visible_text(item_name)
        search_box_dropdown_value = Select(self.drop_down_object).first_selected_option.text
        assert_that(search_box_dropdown_value).is_equal_to(item_name)

        """search book"""
        self.driver.find_element(By.ID, 'twotabsearchtextbox').clear()
        self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(book_name)
        self.driver.find_element(By.ID, 'nav-search-submit-button').send_keys(Keys.ENTER)
        search_box_input_value = self.driver.find_element(By.ID, 'twotabsearchtextbox').get_attribute('value')
        assert_that(search_box_input_value).is_equal_to(book_name)

        assert self.driver.find_element(By.XPATH, '//span[text()="' + search_result + '"]').is_displayed() == True

        self.driver.find_element(By.XPATH, '//span[text()="' + search_result + '"]').click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        """Add quantity to cart"""
        assert_that(search_result).is_equal_to(self.driver.find_element(By.ID, 'productTitle').text)
        book_price = (self.driver.find_element(By.XPATH,
                                               "//span[@class='a-size-base a-color-price a-color-price']").text)
        book_price = int(book_price.replace('₹', '').split('.')[0])
        total_price = book_price * int(quantity)
        Select(self.driver.find_element(By.ID, 'quantity')).select_by_value(str(quantity))
        self.driver.find_element(By.ID, 'add-to-cart-button').click()

        """Go to cart and verify the total price"""
        assert_that(total_price).is_equal_to(int(self.driver.find_element(By.XPATH,
                                                                          "//span[@class='a-price sw-subtotal-amount']//span[@class='a-price-whole']").text))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.LINK_TEXT, "Go to Cart"))

        """Delete the item from the cart and verify message"""
        self.driver.find_element(By.XPATH, "//input[@data-action='delete']").click()
        assert_that(
            self.driver.find_element(By.XPATH, "//h1[contains(text(),'Your Amazon Cart is empty.')]").text).is_equal_to(
            'Your Amazon Cart is empty.')

        assert_that(self.driver.find_element(By.XPATH,
                                             "//div[@class='sc-list-item-removed-msg']/div[@data-action='delete']/span").text).is_equal_to(
            search_result + ' was removed from Shopping Cart.')
