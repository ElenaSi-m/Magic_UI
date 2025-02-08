from pages.sale_page import Sale
from selenium.webdriver.common.by import By


def test_header_title(driver):
    sale_page = Sale(driver)
    sale_page.open_page()
    sale_page.check_page_header_title_is("Sale")

def test_mens_bargains_navigation(driver):
    sale_page = Sale(driver)
    sale_page.open_page()
    sale_page.click_mens_bargains()
    assert "men-sale.html" in driver.current_url, "Navigation to Men's Bargains failed"

def test_get_products_count(driver):
    sale_page = Sale(driver)
    sale_page.open_page()
    assert sale_page.get_products_count() > 0, "No products found on Sale page"
