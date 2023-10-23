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
    list_cart_item = (By.XPATH, "//div[@class='cart_item']")
    button_add_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
    button_remove_bagpack = (By.ID, "remove-sauce-labs-backpack")
    button_remove_bike_light = (By.ID, "remove-sauce-labs-bike-light")
    button_continue_shopping = (By.ID, "continue-shopping")

    """=====================Constructor==========================="""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """=====================Page Functions========================"""

    @allure.step("Check if cart value is empty")
    def initial_cart_count(self):
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
    def add_product_to_cart(self, product_name):
        # product_name = "Sauce Labs Backpack"
        any_product_name = (By.XPATH, "//*[@id='inventory_container']//div[contains(text(),'{}')]".format(product_name))
        self.click_on_element(any_product_name)
        self.click_on_element(self.button_add_bagpack)
        self.take_screenshot()
        self.click_on_element(self.button_shopping_cart)
        assert self.get_element_text(self.cart_product_bagpack_name) == product_name
        self.take_screenshot()

    @allure.step("Check if cart is empty")
    def check_cart_is_empty(self):
        self.is_element_hidden(self.badge_shopping_cart)
        logging.info("Cart is empty on homepage")
        self.click_on_element(self.button_shopping_cart)
        self.is_element_hidden(self.list_cart_item)
        logging.info("Cart is empty")
        self.take_screenshot()

    @allure.step("Add two products to cart")
    def add_two_products_to_cart(self):
        self.click_on_element(self.button_add_bagpack)
        self.click_on_element(self.button_add_bike_light)
        logging.info("Both Backpack and Bike light has been added to the cart")
        self.take_screenshot()

    @allure.step("Verify products in cart")
    def verify_products_in_cart(self):
        self.click_on_element(self.button_shopping_cart)
        logging.info("Navigated to cart")
        elements = self.find_elements(self.cart_product_bagpack_name)
        expected_texts = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
        for i, element in enumerate(elements):
            actual_text = element.text
            expected_text = expected_texts[i]
            assert actual_text == expected_text, f"Text mismatch at element {i + 1}: Expected '{expected_text}', but got '{actual_text}'"
        self.take_screenshot()
        logging.info("Both the product is present in the cart")

    @allure.step("Navigate back to Continue shopping")
    def continue_shopping(self):
        self.click_on_element(self.button_continue_shopping)
        logging.info("Navigated back to product page after clicking on continue shopping")
        self.take_screenshot()

    @allure.step("Remove two products to cart")
    def remove_two_products_to_cart(self):
        self.click_on_element(self.button_remove_bagpack)
        self.click_on_element(self.button_remove_bike_light)
        logging.info("Both Backpack and Bike light has been removed from the cart")
        self.take_screenshot()
