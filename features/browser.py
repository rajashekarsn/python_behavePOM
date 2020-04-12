from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome('/home/shanmukh/Python-3.7.3/chromedriver')
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    def close(self):
        self.driver.close()