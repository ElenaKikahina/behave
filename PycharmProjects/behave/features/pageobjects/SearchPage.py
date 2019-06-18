from selenium.webdriver.common.by import By

from features.pageobjects.BasePage import BasePage


class SearchPage(BasePage):
    locator_dictionary = {
        "book_name": (By.CLASS_NAME, 'product-small-teaser__title'),
#        "not_find_element": (By.CLASS_NAME, 'view-empty'),
        "title_adv": (By.ID, 'edit-field-product-field-title-without-prefix'),
        "search_button_adv": (By.CLASS_NAME, 'form-submit'),
        "author_field_adv": (By.ID, 'edit-field-product-field-author-full-name'),
        "book_author_name": (By.CLASS_NAME, 'product-small-teaser__series')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url="https://rosenclassroom.com")

    def get_find_elements(self):
        self.find_elements(*self.locator_dictionary['book_name'])

#    def get_not_find_element(self):
#        self.find_element(*self.locator_dictionary['not_find_element'])
#
    def find_by_title_adv(self, text):
        self.find_element(*self.locator_dictionary['title_adv']).send_keys(text)

    def click_search_adv(self):
        self.find_element(*self.locator_dictionary['search_button_adv']).click()

    def find_by_author(self, text):
        self.find_element(*self.locator_dictionary['author_field_adv']).send_keys(text)

    def get_find_elements_by_author(self):
        self.find_elements(*self.locator_dictionary['book_author_name'])
