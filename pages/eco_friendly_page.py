from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support import expected_conditions as ec


class EcoFriendly(BasePage):
    page_url = "collections/eco-friendly.html"


    def check_page_header_title_is(self, text):
        header_title = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        assert header_title.text == text, f"Expected header '{text}', but got '{header_title.text}'"
