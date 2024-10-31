from page_objects.home_page import HomePage
from page_objects.authorization_page import AuthorizationPage
import allure
import pytest
from conftest import *
from data import *
from locators import *

class TestHomePage:
    def test_the_transition_by_clicking_on_button_constructor(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.click_on_the_personal_button()
        home_page.click_on_the_button_constructor()
        home_page.assert_home_url()

    def test_the_transition_by_clicking_on_feed_orders(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.click_on_the_feed_orders()
        home_page.assert_feed_orders_url()

    def test_window_appearance(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.click_on_the_pink_bun()
        home_page.checking_that_the_window_is_visible()

    def test_window_close(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.click_on_the_pink_bun()
        home_page.click_on_the_cross()
        home_page.checking_that_the_window_is_not_visible()

    def test_count_increase(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.move_bun()
        home_page.checking_that_the_cost_is_visible()

    def test_create_an_order_login_user(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.move_bun()
        home_page.click_place_an_order()
        home_page.checking_text_your_order_has_begun_to_be_prepared_is_visible()