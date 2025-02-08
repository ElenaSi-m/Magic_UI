from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this class')

    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
