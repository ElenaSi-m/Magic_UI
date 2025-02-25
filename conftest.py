from selenium import webdriver
import pytest
from time import sleep
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    return chrome_driver

@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)

@pytest.fixture()
def sale_page(driver):
    return Sale(driver)
