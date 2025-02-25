from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils import project_ec
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class Sale(BasePage):

    page_url = "sale.html"


    def check_page_header_title_is(self, text):
        header_title = self.find((By.TAG_NAME, "h1"))
        assert header_title.text == text, f"Expected header '{text}', but got '{header_title.text}'"


    def click_mens_bargains(self):
        mens_bargains = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, '//a[@href="https://magento.softwaretestingboard.com'
                                                  '/promotions/men-sale.html"]//strong[contains(text(),'
                                                  ' "Men’s Bargains")]'))
        )
        mens_bargains.click()
        assert "men-sale.html" in self.driver.current_url, "Navigation to Men's Bargains failed"


    def get_products_count(self):
        mens_jackets = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, '//a[@href="https://magento.softwaretestingboard.com'
                                                  '/men/tops-men/jackets-men.html" and contains(text(),'
                                                  ' "Jackets")]'))
        )
        mens_jackets.click()
        products = self.driver.find_elements(By.CSS_SELECTOR, ".product-item")
        assert len(products) > 0, "No products found on Sale page"
        return len(products)
