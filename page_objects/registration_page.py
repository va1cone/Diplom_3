from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *


class RegistrationPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.registration_url = 'https://stellarburgers.nomoreparties.site/register'
        self.authorization_url = 'https://stellarburgers.nomoreparties.site/'
        self.registration_name_entry_field = (By.XPATH, registration_name_entry_field)
        self.registration_email_entry_field = (By.XPATH, registration_email_entry_field)
        self.registration_password_entry_field = (By.XPATH, registration_password_entry_field)
        self.register_button = (By.XPATH, register_button)

    @allure.step("Открытие главной страницы")
    def opening_the_registration_url (self):
        self.open_page(self.registration_url )

    def entering_email_in_the_login_form(self, email: str):
        self.send_keys(*self.registration_email_entry_field, email)

    def entering_name_in_the_login_form(self, name: str):
        self.send_keys(*self.registration_name_entry_field, name)

    def entering_password_in_the_login_form(self, password: str):
        self.send_keys(*self.registration_password_entry_field, password)

    def click_on_the_register_button(self):
        self.click(*self.register_button)
