import time

import pytest
from selenium import webdriver


class AmazonConfig:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.amazon.in/")

        yield
        time.sleep(3)
        self.driver.quit()
