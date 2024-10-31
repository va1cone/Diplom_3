from page_objects.forgot_password_page import ForgotPasswordPage
import allure
import pytest
from conftest import *
from data import *
from locators import *

class TestForgotPasswordPage:
    def test_go_to_the_password_recovery(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.opening_the_login_page()
        forgot_password_page.click_on_the_reset_password_button()
        forgot_password_page.assert_forgot_password_url()

    def test_enter_email_and_click_on_the_restore_button(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.opening_the_login_page()
        forgot_password_page.click_on_the_reset_password_button()
        forgot_password_page.entering_email_in_the_password_recovery_form(test_email)
        forgot_password_page.click_on_the_reset_password_button_on_the_recovery_page()
        forgot_password_page.assert_reset_password_url()

    def test_clicking_the_show_password_button_makes_the_field_active(self, driver): #сначала неправильно прочитала заданиe, сделала не тот тест)) но пусть будет
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.opening_the_login_page()
        forgot_password_page.click_on_the_reset_password_button()
        forgot_password_page.entering_email_in_the_password_recovery_form(test_email)
        forgot_password_page.click_on_the_reset_password_button_on_the_recovery_page()
        forgot_password_page.entering_password_in_the_password_recovery(test_password)
        forgot_password_page.checking_that_the_hidden_password_is_visible()
        forgot_password_page.click_on_the_eye_button()

    def test_the_recovery_form_is_active(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.opening_the_login_page()
        forgot_password_page.click_on_the_reset_password_button()
        forgot_password_page.entering_email_in_the_password_recovery_form(test_email)
        forgot_password_page.click_on_the_reset_password_button_on_the_recovery_page()
        forgot_password_page.entering_password_in_the_password_recovery(test_password)
        forgot_password_page.click_on_the_eye_button()
        forgot_password_page.checking_that_the_recovery_form_is_active()

    













