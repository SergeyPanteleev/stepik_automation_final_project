from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_area = self.browser.find_element(*LoginPageLocators.EMAIL_AREA)
        email_area.send_keys(email)
        password1_area = self.browser.find_element(*LoginPageLocators.PASSWORD1_AREA)
        password1_area.send_keys(password)
        password2_area = self.browser.find_element(*LoginPageLocators.PASSWORD2_AREA)
        password2_area.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
