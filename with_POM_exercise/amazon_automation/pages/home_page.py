import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from with_POM_exercise.amazon_automation.constants.constants import locator, locator_path


class HomePage(object):
    def __init__(self, driver):
        print('setting driver')
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        print('waiting for dropdown')
        self.drop_down_object = self.wait.until(
            ec.presence_of_element_located((locator['id'],
                                            locator_path['drop_down_menu']
                                            )))

        self.drop_down = Select(self.drop_down_object)
        self.search_box = driver.find_element(locator['id'],
                                              locator_path['search_box'])
        self.search_result = ''

    def get_drop_down(self):
        return self.drop_down

    def get_search_box(self):
        return self.search_box

    def set_search_box(self, value):
        print('entering value in search box')
        self.search_box.clear()
        self.search_box.send_keys(value)
        self.search_box.send_keys(Keys.ENTER)

    def get_search_result(self):
        print('Waiting for all books is appeared..')
        return self.wait.until(
            ec.visibility_of_element_located((locator['xpath'],
                                              locator_path[
                                                  'search_result']
                                              )))

    def select_book(self):
        print('waiting for particular book is appeared......')
        book = self.wait.until(ec.element_to_be_clickable((
            locator['partial_link_text'],
            'The Secret of The Nagas (Shiva Trilogy Book 2) (Shiva, 2)'
        )))
        book.click()
