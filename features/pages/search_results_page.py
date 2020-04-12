from features.browser import Browser
from selenium.webdriver.common.by import By


class SearchResultsPageLocator(object):
    # Search Page Locators
    LINKS_DIV = (By.XPATH, '//div')


class SearchResultsPage(Browser):
    # Search Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def get_links(self):
        return self.driver.find_elements(*SearchResultsPageLocator.LINKS_DIV)

    def find_search_result(self, phrase):
        return self.get_element(By.PARTIAL_LINK_TEXT, phrase)



