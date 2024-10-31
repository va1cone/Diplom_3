from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.home_url = 'https://stellarburgers.nomoreparties.site/'
        self.button_constructor = (By.XPATH, button_constructor)
        self.feed_orders_url = 'https://stellarburgers.nomoreparties.site/feed'
        self.personal_account_button = (By.XPATH, personal_account_button)
        self.feed_orders = (By.XPATH, feed_orders)
        self.pink_bun = (By.XPATH, pink_bun)
        self.window_with_details = (By.XPATH, window_with_details)
        self.cross = (By.XPATH, cross)
        self.cross_orders = (By.XPATH, cross_orders)
        self.place_to_move_the_bun = (By.XPATH, place_to_move_the_bun)
        self.cost_of_two_buns = (By.XPATH, cost_of_two_buns)
        self.button_place_an_order = (By.XPATH, button_place_an_order)
        self.text_your_order_has_begun_to_be_prepared = (By.XPATH, text_your_order_has_begun_to_be_prepared)


    def click_on_the_personal_button(self):
        self.click(*self.personal_account_button)

    @allure.step("Открытие главной страницы")
    def click_on_the_button_constructor(self):
        self.click(*self.button_constructor)

    def assert_home_url(self):
        self.wait_for_url(self.home_url)
        self.assert_current_url(self.home_url)

    def click_on_the_feed_orders(self):
        self.click(*self.feed_orders)

    def assert_feed_orders_url(self):
        self.wait_for_url(self.feed_orders_url)
        self.assert_current_url(self.feed_orders_url)

    def click_on_the_pink_bun(self):
        self.click(*self.pink_bun)

    def checking_that_the_window_is_visible(self):
        self.wait_until_visible(*self.window_with_details)

    def click_on_the_cross(self):
        self.click(*self.cross)

    def checking_that_the_window_is_not_visible(self):
        self.wait_until_invisible(*self.window_with_details)

    def move_bun(self):
        source_value = self.pink_bun[1]
        target_value = self.place_to_move_the_bun[1]

        self.drag_and_drop_bun(source_value, target_value)

    def checking_that_the_cost_is_visible(self):
        self.wait_until_visible(*self.cost_of_two_buns)

    def click_place_an_order(self):
        self.click(*self.button_place_an_order)

    def checking_text_your_order_has_begun_to_be_prepared_is_visible(self):
        self.wait_until_visible(*self.text_your_order_has_begun_to_be_prepared)

    def click_cross_orders(self):
        self.click(*self.cross_orders)


