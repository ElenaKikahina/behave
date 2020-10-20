from selenium.webdriver.common.by import By

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.select import Select
import time


class SearchPage(BasePage):
    locator_dictionary = {
        "book_teaser_title_field": (By.CLASS_NAME, 'product-small-teaser__title'),
        "title_advanced_search_field": (By.ID, 'edit-field-product-field-title-without-prefix'),
        "advanced_search_button": (By.ID, 'edit-submit-cavendishsq-display-products'),
        "author_advanced_search_field": (By.ID, 'edit-field-product-field-author-full-name'),
        "book_author_name": (By.CLASS_NAME, 'product-small-teaser__series'),
        "not_search_message_field": (By.CLASS_NAME, 'view-empty'),
        "format_field_advanced": (By.ID, 'edit-search-api-views-fulltext-1'),
        "format_field_dropdown": (By.XPATH, "//select[@id='edit-search-api-views-fulltext-1']"),
        "book_format_field": (By.CLASS_NAME, "form-control")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url="https://rosenclassroom.com")

    def get_find_teaser_title_text(self):
        book_teaser_title = self.find_element(*self.locator_dictionary['book_teaser_title_field']).text
        return book_teaser_title


    def open_book_page(self):
        self.find_element(*self.locator_dictionary['book_teaser_title_field']).click()
        time.sleep(10)
        new_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(new_tab)
        time.sleep(10)


    def get_find_element_by_title(self):
        self.find_element(*self.locator_dictionary['book_name'])

    def find_by_title_advanced(self, text):
        self.find_element(*self.locator_dictionary['title_advanced_search_field']).send_keys(text)

    def display_advanced_search_results(self):
        self.find_element(*self.locator_dictionary['advanced_search_button']).click()
        time.sleep(10)

    def find_by_author_advanced(self, text):
        self.find_element(*self.locator_dictionary['author_advanced_search_field']).send_keys(text)

    def get_find_elements_by_author(self):
        self.find_elements(*self.locator_dictionary['book_author_name'])

    def get_not_search_message(self):
        not_results_found = self.find_element(*self.locator_dictionary['not_search_message_field']).text
        return not_results_found

    def find_by_format_advanced(self):
        self.find_element(*self.locator_dictionary['format_field_advanced']).click()

    def get_format_in_dropdown(self):
        select_format = Select(self.find_element(*self.locator_dictionary['format_field_dropdown']))
        select_format.select_by_index(16)
        time.sleep(10)


    def get_books_with_format(self):
        all_list = self.find_elements(*self.locator_dictionary['book_format_field'])
        results = [x.text for x in all_list if len(x.text) > 0]
        return results
