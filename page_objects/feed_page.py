from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *


class FeedPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        #self.profile_url = 'https://stellarburgers.nomoreparties.site/account/profile'
        self.the_first_order_on_the_list = (By.XPATH, the_first_order_on_the_list)
        self.order_modal_window = (By.XPATH, order_modal_window)
        #self.history_orders_button = (By.XPATH, history_orders_button)

    @allure.step("Открытие главной страницы")
    def click_on_the_first_order_on_the_list(self):
        self.click(*self.the_first_order_on_the_list)

    def checking_that_the_order_modal_window_is_visible(self):
        self.wait_until_visible(*self.order_modal_window)