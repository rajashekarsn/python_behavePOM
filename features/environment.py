from features.browser import Browser
from features.pages.home_page import HomePage
from features.pages.search_results_page import SearchResultsPage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()


def after_all(context):
    context.browser.close()

#   #  non POM model
# def before_all(context):
#     context.browser = webdriver.Chrome('/home/shanmukh/Python-3.7.3/chromedriver')
#     context.browser.set_page_load_timeout(10)
#     context.browser.implicitly_wait(5)
#     """An implicit wait tells WebDriver to poll the DOM for a certain amount of time
#     when trying to find any element (or elements) not immediately available.
#     The default setting is 0. Once set, the implicit wait is set for the life of the WebDriver object."""
#     context.browser.maximize_window()
#
#
# def after_all(context):
#     context.browser.quit()

