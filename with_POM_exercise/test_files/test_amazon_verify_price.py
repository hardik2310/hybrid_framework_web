import time

from with_POM_exercise.amazon_automation.pages.book_page import BookPage
from with_POM_exercise.amazon_automation.pages.home_page import HomePage
from with_POM_exercise.config.conftest import AmazonConfig


class TestAmazonHomePage(AmazonConfig):
    def test_home_page(self):
        try:
            print(self.driver.title)
            home_page = HomePage(self.driver)
            drop_down = home_page.get_drop_down()
            all_option = drop_down.options
            for option in all_option:
                if option.text == 'Books':
                    print(option.text + ' is selected from dropdown..')
                    option.click()
                    break

            print('title of the main page :: ' + self.driver.title)
            home_page.set_search_box('Shiva Triology')
            # Verify books are displayed.
            home_page.get_search_result()
            print('all books appeared....')
            home_page.select_book()

        except BaseException as e:
            print('exception occurred in home page :: ', e)

        try:
            all_windows = self.driver.window_handles
            all_windows.remove(self.driver.current_window_handle)
            for window in all_windows:
                self.driver.switch_to.window(window)
                self.driver.implicitly_wait(3)
                if self.driver.title == 'Buy The Secret Of The Nagas (Shiva Trilogy-2) Book ' \
                                        'Online at Low Prices in India | The Secret Of The ' \
                                        'Nagas (Shiva Trilogy-2) Reviews & Ratings - Amazon.in':
                    break
            print('title of the new page :: ' + self.driver.title)
            book_page = BookPage(self.driver)
            assert book_page.get_book_price() == '₹210.00'

            assert book_page.get_original_price() == '₹799.00'

            assert '74%' in book_page.get_discount()
        except Exception as e:
            print('exception occurred in verify price :: ', e)
