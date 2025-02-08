from pages.eco_friendly_page import EcoFriendly
from selenium.webdriver.common.by import By

def test_header_title(driver):
    eco_friendly_page = EcoFriendly(driver)
    eco_friendly_page.open_page()
    eco_friendly_page.check_page_header_title_is("Eco Friendly")

def test_check_add_cart_button_first_product(driver):
    eco_friendly_page = EcoFriendly(driver)
    eco_friendly_page.open_page()
    first_product_button = eco_friendly_page.find(
        (By.CSS_SELECTOR, ".products-grid .product-item:first-child button.tocart"))
    assert first_product_button.is_displayed(), "Button 'Add to Cart' is missing at the first product"


def test_products_are_displayed(driver):
    eco_friendly_page = EcoFriendly(driver)
    eco_friendly_page.open_page()
    products = eco_friendly_page.find_elements((By.CSS_SELECTOR, ".products-grid .product-item"))
    assert len(products) > 0, "Products are not displayed on this page"
