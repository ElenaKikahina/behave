from selenium.webdriver.common.by import By

from features.pageobjects.BasePage import BasePage


class HomePage(BasePage):
    # logo = By.CSS_SELECTOR('#node-17 .content')
    locator_dictionary = {
        "logo": (By.CSS_SELECTOR, '#node-17 .content'),
        "password": (By.ID, 'passwd'),
        "signin_button": (By.ID, 'SubmitLogin'),
        "search": (By.CLASS_NAME, 'search-input'),
        "search_button": (By.CSS_SELECTOR, '#search-box-menu > div.clearfix > button > i'),
        "book_name": (By.CLASS_NAME, 'product-small-teaser__title')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url="https://rosenclassroom.com")

    def click_logo(self):
        self.find_element(*self.locator_dictionary['logo']).click()

    def find_by_title(self, text):
        self.find_element(*self.locator_dictionary['search']).send_keys(text)

    def click_search(self):
        self.find_element(*self.locator_dictionary['search_button']).click()

    def find_by_isbn(self, text):
        self.find_element(*self.locator_dictionary['search']).send_keys(text)

    def click_book_name(self):
        self.find_element(*self.locator_dictionary['book_name']).click()
