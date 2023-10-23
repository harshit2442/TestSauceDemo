import logging
import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from KeywordLibrary.keyword import GenericMethods


class SauceDemoPage(GenericMethods):
    """======================Locator=============================="""

    search_textbox = (By.NAME, "q")
    search_button = (By.NAME, "btnk")
    google_cookies_popup = (By.XPATH, "//+[text()='Accept all']")
    field_username = (By.ID, "user-name")
    field_password = (By.ID, "password")
    button_login = (By.ID, "login-button")
    logo = (By.XPATH, "//div[contains(text(), 'Swag Labs')]")
    button_menubar = (By.ID, "react-burger-menu-btn")
    button_logout = (By.ID, "logout_sidebar_link")
    message_error = (By.XPATH, "//*[@id='login_button_container']//h3")

    """=====================Constructor==========================="""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """=====================Page Functions========================"""

    @allure.step("Navigate to page")
    def navigate_to_page(self, url):
        self.navigate(url)
        if self.is_element_present(self.google_cookies_popup):
            self.click_on_element(self.google_cookies_popup)
        logging.info("Navigated successfully to : %s" % url)
        self.take_screenshot()

    @allure.step("Login to Page")
    def login_to_page(self, username, password):
        self.enter_text(self.field_username, username)
        self.enter_text(self.field_password, password)
        self.click_on_element(self.button_login)
        assert self.get_element_text(self.logo) == "Swag Labs"
        logging.info("Logged in successfully")
        self.take_screenshot()

    @allure.step("Logout of page")
    def logout_of_page(self):
        self.click_on_element(self.button_menubar)
        self.click_on_element(self.button_logout)
        assert self.is_element_present(self.field_username)
        logging.info("Logged out successfully")
        self.take_screenshot()

    @allure.step("Login to Page")
    def login_to_page_with_invalid_username_password(self, username, password):
        self.enter_text(self.field_username, username)
        self.enter_text(self.field_password, password)
        self.click_on_element(self.button_login)
        assert self.get_element_text(self.message_error) == "Epic sadface: Username and password do not match any user in this service"
        logging.info("Unable to login because of Invalid username or Invalid password")
        self.take_screenshot()
