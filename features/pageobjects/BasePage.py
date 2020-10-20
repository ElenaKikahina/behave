from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import time


class BasePage(object):

    def __init__(self, browser, base_url):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 1000000

    def get_url(self):
        return self.browser.current_url

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def find_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def visit(self, url):
        self.browser.get(url)

    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()
        time.sleep(5)

    # def switch(self, new_window=str(f'window.open("https://rosenclassroom.com/")')):
    #     # self.browser.switch_to_window(window_name='')
    #     var = self.browser.window_handles
    #     current_window = self.browser.current_window_handle
    #     self.browser.switch_to.window(new_window)

    def __getattr__(self, what) -> object:
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print("No %s here!" % what)
