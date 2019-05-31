from features.locators.locators import Locators


class Logo():

    def __init__(self, driver):
        self.driver = driver
        #        self.driver.get ("https://rosenclassroom.com")

        self.logo_id = Locators.logo_id

    def click_logo(self):
        self.driver.find_element_by_css(self.logo_id).click()

#    def logo(self):
#        self.driver.find_element_by_id(self, id(node-17))
#        return None
#
#
# class MainPageLocators(object):
#    LOGO = (By.ID, 'node-17')
#
#   def logo(self):
#       print('Click logo button')
#
# class Logo():
#    LOGIN = 'node-17'
#
#    def click_logo_button(self):
#        self.click(id=self.LOGIN)
#        return Logo(self.driver)
