import logging
import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from KeywordLibrary.keyword import GenericMethods


class SauceDemoProductPage(GenericMethods):
    """======================Locator=============================="""

    button_add_bagpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    badge_shopping_cart = (By.XPATH, "//*[@id='shopping_cart_container']/a/span")
    button_shopping_cart = (By.XPATH, "//*[@id='shopping_cart_container']/a")
    cart_product_bagpack_name = (By.XPATH, "//*[@class='inventory_item_name']")
    any_product_name = (By.XPATH, "//*[@id='inventory_container']//div[contains(text(),'{}')]")

    """=====================Constructor==========================="""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """=====================Page Functions========================"""

    @allure.step("check if cart is empty")
    def initial_bagpack_count(self):
        self.is_element_hidden(self.badge_shopping_cart)
        logging.info("Cart is empty")
        self.take_screenshot()

    @allure.step("Add Bagback to cart")
    def add_bagpack_to_cart(self):
        self.click_on_element(self.button_add_bagpack)
        self.take_screenshot()
        self.click_on_element(self.button_shopping_cart)
        assert self.get_element_text(self.cart_product_bagpack_name) == "Sauce Labs Backpack"
        self.take_screenshot()

    @allure.step("Add specific product to cart")
    def add_product_to_cart(self,product_name):
        # product_name = "Sauce Labs Backpack"
        any_product_name = (By.XPATH, "//*[@id='inventory_container']//div[contains(text(),'{}')]".format(product_name))
        self.click_on_element(any_product_name)
        self.click_on_element(self.button_add_bagpack)
        self.take_screenshot()
        self.click_on_element(self.button_shopping_cart)
        assert self.get_element_text(self.cart_product_bagpack_name) == product_name
        self.take_screenshot()
