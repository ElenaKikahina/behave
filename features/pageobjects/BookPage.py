from selenium.webdriver.common.by import By
import re

from features.pageobjects.BasePage import BasePage


class BookPage(BasePage):
    locator_dictionary = {
        "book_isbn_field": (By.XPATH, "//div[contains(@class, 'small-meta-item')][2]"),
        "book_author_field": (By.XPATH, "//div[contains(@class, 'small-meta-item')][3]")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url="https://rosenclassroom.com")

    def get_book_isbn_info(self):
        book_isbn_text = self.find_element(*self.locator_dictionary['book_isbn_field']).text
        book_isbn_text = re.sub("^\s+|\n|\r|\s+$", '', book_isbn_text)
        return book_isbn_text

    def get_book_author_name(self):
        book_author_text = self.find_element(*self.locator_dictionary['book_author_field']).text
        book_author_text = re.sub("^\s+|\n|\r|\s+$", '', book_author_text)
        return book_author_text