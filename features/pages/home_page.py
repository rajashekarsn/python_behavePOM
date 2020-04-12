from selenium.webdriver.common.keys import Keys

from features.browser import Browser
from selenium.webdriver.common.by import By


class HomePageLocator(object):
    # Home Page Locators
    SEARCH_BOX = (By.NAME, 'q')
    # SUBMIT_BUTTON = (By.ID, 'search_button_homepage')


class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text + Keys.RETURN)
    #     Keys.Return - is for pressing "enter" in the keyboard

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_BOX)
        # self.click_element(*HomePageLocator.SUBMIT_BUTTON)

