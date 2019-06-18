from selenium.webdriver.common.by import By

from features.pageobjects.BasePage import BasePage


class BookPage(BasePage):
    locator_dictionary = {
        "book_info": (By.CSS_SELECTOR, 'div.small-meta > div:nth-child(2)')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url="https://rosenclassroom.com")

    def get_find_isbn(self, text):
        self.find_element(*self.locator_dictionary['book_info']).click(text)