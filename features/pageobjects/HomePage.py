from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from features.pageobjects.BasePage import BasePage
import time

class HomePage(BasePage):
    # logo = By.CSS_SELECTOR('#node-17 .content')
    locator_dictionary = {
        "site_logo": (By.CSS_SELECTOR, '#node-17 .content'),
        # "password": (By.ID, 'passwd'),
        # "signin_button": (By.ID, 'SubmitLogin'),
        "search_field": (By.CLASS_NAME, 'search-input'),
        "search_button": (By.CLASS_NAME, 'search-submit'),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url="https://rosenclassroom.com")

    def click_logo(self):
        self.find_element(*self.locator_dictionary['site_logo']).click()

    def find_by_query_in_search_field(self, text):
        self.find_element(*self.locator_dictionary['search_field']).send_keys(text)

    def display_simple_search_results(self):
        self.find_element(*self.locator_dictionary['search_button']).click()
        time.sleep(10)

    def find_book_title(self, text):
        self.find_element(*self.locator_dictionary['book_title']).send_keys(text)
