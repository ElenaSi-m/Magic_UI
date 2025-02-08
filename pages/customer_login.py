from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils import project_ec
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from pages.locators import login_locators as loc


class CustomerLogin(BasePage):

    page_url = "customer/account/create/"

    def fill_login_form(self, firstname, lastname, email, password, password_conf):
        firstname_field = self.find(loc.firstname_field_loc)
        lastname_field = self.find(loc.lastname_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        confirm_password_field = self.find(loc.confirm_password_field_loc )
        button = self.find(loc.button_loc)

        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password_conf)
        button.click()


    def check_error_alert_text_is(self,text):
        error_alert = WebDriverWait(self.driver, timeout=10).until(ec.presence_of_element_located((By.ID, "email_address-error"))
        )
        WebDriverWait(self.driver, timeout=5).until(project_ec.text_is_not_empty_in_element(error_alert))
        assert error_alert.text == text

    def check_error_alert_incorrect_password_is(self,password):
        error_alert = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "password-confirmation-error"))
        )
        WebDriverWait(self.driver, timeout=5).until(project_ec.text_is_not_empty_in_element(error_alert))
        assert error_alert.text == password

    def check_error_alert_weak_password_is(self,password):
        error_alert = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "password-error"))
        )
        WebDriverWait(self.driver, timeout=5).until(project_ec.text_is_not_empty_in_element(error_alert))
        assert error_alert.text == password
