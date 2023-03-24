from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from with_POM_exercise.amazon_automation.constants.constants import locator, locator_path


class BookPage(object):
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 10)
        self.book_price = wait.until(ec.visibility_of_element_located((
            locator['id'],
            locator_path['book_price']
        )))
        self.original_price = driver.find_element(
            locator['id'], locator_path['original_price'])
        self.discount = driver.find_element(
            locator['id'], locator_path['discount'])

    def get_original_price(self):
        return self.original_price.text

    def get_book_price(self):
        return self.book_price.text

    def get_discount(self):
        return self.discount.text
