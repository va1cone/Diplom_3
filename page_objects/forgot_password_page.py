from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *


class ForgotPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.login_url = 'https://stellarburgers.nomoreparties.site/login'
        self.forgot_password_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
        self.reset_password_url = 'https://stellarburgers.nomoreparties.site/reset-password'
        self.recover_password_button = (By.XPATH, recover_password_button)
        self.password_recovery_input_field = (By.XPATH, password_recovery_input_field)
        self.active_password_entry_field_window_in_the_password_recovery_form = (By.XPATH, active_password_entry_field_window_in_the_password_recovery_form)
        self.reset_password_button_on_the_recovery_page = (By.XPATH, reset_password_button_on_the_recovery_page)
        self.entering_password_in_the_password_recovery_form = (By.XPATH, entering_password_in_the_password_recovery_form)
        self.eye_button = (By.XPATH, eye_button)
        self.password_recovery_input_field_hidden = (By.XPATH, password_recovery_input_field_hidden)

    @allure.step("Открытие главной страницы")
    def opening_the_login_page(self):
        self.open_page(self.login_url)

    def click_on_the_reset_password_button(self):
        self.click(*self.recover_password_button)

    def assert_forgot_password_url(self):
        self.assert_current_url(self.forgot_password_url)

    def entering_email_in_the_password_recovery_form(self, email: str):
        self.send_keys(*self.password_recovery_input_field, email)

    def click_on_the_reset_password_button_on_the_recovery_page(self):
        self.click(*self.reset_password_button_on_the_recovery_page)

    def assert_reset_password_url(self):
        self.wait_for_url(self.reset_password_url)
        self.assert_current_url(self.reset_password_url)

    def entering_password_in_the_password_recovery(self, password: str):
        self.send_keys(*self.entering_password_in_the_password_recovery_form, password)

    def click_on_the_eye_button(self):
        self.long_press(*self.eye_button, 1)

    def checking_that_the_hidden_password_is_visible(self):
        self.wait_until_visible(*self.password_recovery_input_field_hidden)

    def checking_that_the_recovery_form_is_active(self):
        self.wait_until_visible(*self.active_password_entry_field_window_in_the_password_recovery_form)


















