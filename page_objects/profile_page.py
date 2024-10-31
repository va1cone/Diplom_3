from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *


class ProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.profile_url = 'https://stellarburgers.nomoreparties.site/account/profile'
        self.order_history_url = 'https://stellarburgers.nomoreparties.site/account/order-history'
        self.personal_account_button = (By.XPATH, personal_account_button)
        self.login_url = 'https://stellarburgers.nomoreparties.site/login'
        self.exit_button = (By.XPATH, exit_button)
        self.history_orders_button = (By.XPATH, history_orders_button)

    @allure.step("Открытие главной страницы")
    def click_on_the_personal_account_button(self):
        self.click(*self.personal_account_button)

    def assert_profile_url(self):
        self.wait_for_url(self.profile_url)
        self.assert_current_url(self.profile_url)

    def click_on_the_history_orders_button(self):
        self.click(*self.history_orders_button)

    def assert_order_history_url(self):
        self.wait_for_url(self.order_history_url)
        self.assert_current_url(self.order_history_url)

    def click_on_the_exit_button(self):
        self.click(*self.exit_button)

    def assert_login_url(self):
        self.wait_for_url(self.login_url)
        self.assert_current_url(self.login_url)