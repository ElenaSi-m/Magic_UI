from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support import expected_conditions as ec


class EcoFriendly(BasePage):
    page_url = "collections/eco-friendly.html"


    def check_page_header_title_is(self, text):
        header_title = self.find((By.TAG_NAME, "h1"))
        assert header_title.text == text, f"Expected header '{text}', but got '{header_title.text}'"

    def check_first_product_button(self):
        first_product_button = self.find(
            (By.CSS_SELECTOR, ".products-grid .product-item:first-child button.tocart"))
        assert first_product_button.is_displayed(), "Button 'Add to Cart' is missing at the first product"

    def check_if_have_products(self):
        products = self.find_elements((By.CSS_SELECTOR, ".products-grid .product-item"))
        assert len(products) > 0, "Products are not displayed on this page"
