import logging
import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from KeywordLibrary.keyword import GenericMethods


class SauceDemoCartPage(GenericMethods):
    """======================Locator=============================="""

    button_checkout = (By.ID, "checkout")
    textbox_first_name = (By.ID, "first-name")
    textbox_last_name = (By.ID, "last-name")
    textbox_zipcode = (By.ID, "postal-code")
    button_continue = (By.ID, "continue")
    cart_product_name = (By.XPATH, "//*[@class='inventory_item_name']")
    button_finish = (By.ID, "finish")
    text_header = (By.XPATH, "//div[@id='checkout_complete_container']/h2")
    text_complete_message = (By.XPATH, "//div[@id='checkout_complete_container']/div")
    message_error = (By.XPATH, "//*[@id='checkout_info_container']//div[4]/h3")

    """=====================Constructor==========================="""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """=====================Page Functions========================"""

    @allure.step("click on checkout")
    def click_on_checkout(self):
        self.click_on_element(self.button_checkout)
        self.take_screenshot()
        logging.info("Checkout button is clicked")

    @allure.step("Shipment details")
    def enter_valid_shipping_details(self, first_name, last_name, zipcode):
        self.enter_text(self.textbox_first_name, first_name)
        self.enter_text(self.textbox_last_name, last_name)
        self.enter_text(self.textbox_zipcode, zipcode)
        self.click_on_element(self.button_continue)
        self.take_screenshot()
        logging.info("Details are filled and clicked on continue")

    @allure.step("Verify products while checkout")
    def verify_products_while_checkout(self):
        elements = self.find_elements(self.cart_product_name)
        expected_texts = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
        for i, element in enumerate(elements):
            actual_text = element.text
            expected_text = expected_texts[i]
            assert actual_text == expected_text, f"Text mismatch at element {i + 1}: Expected '{expected_text}', but got '{actual_text}'"
        self.take_screenshot()
        logging.info("Both the product is present while checkout")

    @allure.step("Place order")
    def place_order_and_verify(self):
        self.click_on_element(self.button_finish)
        header_expected_text = "Thank you for your order!"
        assert self.get_element_text(self.text_header) == header_expected_text
        time.sleep(2)
        complete_text = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        logging.info(self.get_element_text(self.text_complete_message))
        assert self.get_element_text(self.text_complete_message) == complete_text
        logging.info("Order placed successfully")
        self.take_screenshot()

    @allure.step("click on continue without any details")
    def click_on_continue_without_any_details(self):
        self.click_on_element(self.button_continue)
        assert self.get_element_text(self.message_error) == "Error: First Name is required"
        logging.info("Unable to proceed to final checkout page as shipment details are incorrect")
        self.take_screenshot()

    @allure.step("click on continue with empty cart")
    def click_on_continue_with_empty_cart(self):
        assert self.is_element_hidden(self.button_checkout)
        self.take_screenshot()
        logging.info("User should not able to proceed as cart is empty")
