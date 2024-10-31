from page_objects.feed_page import FeedPage
from page_objects.authorization_page import AuthorizationPage
from page_objects.registration_page import RegistrationPage
from page_objects.home_page import HomePage
import allure
import pytest
from conftest import *
from data import *
from locators import *

class TestProfilePage:
    def test_the_transition_by_clicking_on_personal_account(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.click_on_the_feed_orders()
        feed_page = FeedPage(driver)
        feed_page.click_on_the_first_order_on_the_list()
        feed_page.checking_that_the_order_modal_window_is_visible()

    def test_the_order_matches_the_feed_and_history(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.opening_the_registration_url()
        registration_page.entering_name_in_the_login_form(test_name)
        registration_page.entering_email_in_the_login_form(new_email)
        registration_page.entering_password_in_the_login_form(test_password)
        registration_page.click_on_the_register_button()
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(new_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.move_bun()
        home_page.click_place_an_order()
        home_page.click_on_the_feed_orders()

