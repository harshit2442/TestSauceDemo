"""
This Page contains all generic methods that will be used in automating a page
"""
import logging

import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config import config_data


class GenericMethods(object):
    template = "An exception of type {0} occurred. Arguments: \n{1!r}"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Generic function
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_enabled(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self):
        get_title = self.driver.title
        return get_title

    def enter_text_and_enter(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        self.driver.send_keys(Keys.ENTER)

    def navigate(self, url):
        try:
            self.driver.get(url)
            logging.info("--------Navigated to : " + url)
        except Exception as err:
            logging.error("-------unable to navigate to : " + url)
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def is_element_present(self, locator):
        try:
            element = WebDriverWait(self.driver, config_data.globalWaitTime).until(
                EC.visibility_of_element_located(locator))
            logging.info("---------Element is present: " + str(locator[0]) + str(locator[1]))
            return bool(element)
        except:
            logging.error("---------Element is not present: " + str(locator[0]) + str(locator[1]))

    def take_screenshot(self):
        try:
            if config_data.enableScreeshot == "true":
                screenshot = self.driver.get_screenshot_as_png()
                allure.attach(screenshot, name='Screenshot', attachment_type=AttachmentType.PNG)
                logging.info("Screenshot taken and attached to Allure report.")
        except Exception as err:
            logging.error("Unable to take screenshot.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def find_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            logging.info(f"Found element: {locator}")
            return element
        except Exception as err:
            logging.error(f"Element not found: {locator}")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def scroll_to_element(self, locator):
        try:
            element = WebDriverWait(self.driver, config_data.globalWaitTime).until(
                EC.visibility_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()
            logging.info(f"Scrolled to element: {locator}")
        except Exception as err:
            logging.error(f"Failed to scroll to element: {locator}")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    # Click on Element using JavaScript:
    def click_on_element_js(self, locator):
        try:
            element = WebDriverWait(self.driver, config_data.globalWaitTime).until(
                EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)
            logging.info(f"Clicked on element using JavaScript: {locator}")
        except Exception as err:
            logging.error(f"Failed to click on element using JavaScript: {locator}")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def get_attribute_value(self, locator, attribute_name):
        try:
            element = WebDriverWait(self.driver, config_data.globalWaitTime).until(
                EC.visibility_of_element_located(locator))
            attribute_value = element.get_attribute(attribute_name)
            logging.info(f"Attribute '{attribute_name}' value of element {locator}: {attribute_value}")
            return attribute_value
        except Exception as err:
            logging.error(f"Failed to get attribute '{attribute_name}' value of element {locator}")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def wait_for_element_to_be_clickable(self, locator):
        try:
            element = WebDriverWait(self.driver, config_data.globalWaitTime).until(
                EC.element_to_be_clickable(locator))
            logging.info(f"Element is clickable: {locator}")
            return element
        except Exception as err:
            logging.error(f"Element is not clickable: {locator}")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def is_element_selected(self, locator):
        try:
            element = WebDriverWait(self.driver, config_data.globalWaitTime).until(
                EC.visibility_of_element_located(locator))
            is_selected = element.is_selected()
            logging.info(f"Is element {locator} selected? {is_selected}")
            return is_selected
        except Exception as err:
            logging.error(f"Failed to check if element {locator} is selected")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def handle_alert(self, accept=True):
        try:
            alert = WebDriverWait(self.driver, config_data.globalWaitTime).until(EC.alert_is_present())
            if accept:
                alert.accept()
                logging.info("Accepted the alert.")
            else:
                alert.dismiss()
                logging.info("Dismissed the alert.")
        except Exception as err:
            logging.error("Failed to handle the alert.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def switch_to_window_by_handle(self, window_handle):
        try:
            self.driver.switch_to.window(window_handle)
            logging.info(f"Switched to window with handle: {window_handle}")
        except Exception as err:
            logging.error(f"Failed to switch to window with handle: {window_handle}")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def switch_to_window_by_title(self, window_title):
        try:
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                if self.driver.title == window_title:
                    logging.info(f"Switched to window with title: {window_title}")
                    return
            logging.warning(f"No window found with title: {window_title}")
        except Exception as err:
            logging.error(f"Failed to switch to window with title: {window_title}")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
            logging.info("Switched to default content.")
        except Exception as err:
            logging.error("Failed to switch to default content.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def get_current_url(self):
        try:
            current_url = self.driver.current_url
            logging.info(f"Current URL: {current_url}")
            return current_url
        except Exception as err:
            logging.error("Failed to get current URL.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def select_option_by_text(self, locator, option_text):
        try:
            select_element = Select(self.find_element(locator))
            select_element.select_by_visible_text(option_text)
            logging.info(f"Selected option '{option_text}' from dropdown.")
        except Exception as err:
            logging.error(f"Failed to select option '{option_text}' from dropdown.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def select_option_by_value(self, locator, option_value):
        try:
            select_element = Select(self.find_element(locator))
            select_element.select_by_value(option_value)
            logging.info(f"Selected option with value '{option_value}' from dropdown.")
        except Exception as err:
            logging.error(f"Failed to select option with value '{option_value}' from dropdown.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def select_option_by_index(self, locator, option_index):
        try:
            select_element = Select(self.find_element(locator))
            select_element.select_by_index(option_index)
            logging.info(f"Selected option at index {option_index} from dropdown.")
        except Exception as err:
            logging.error(f"Failed to select option at index {option_index} from dropdown.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def is_element_displayed(self, locator):
        try:
            element = self.find_element(locator)
            is_displayed = element.is_displayed()
            if is_displayed:
                logging.info(f"Element {locator} is displayed.")
            else:
                logging.info(f"Element {locator} is not displayed.")
            return is_displayed
        except Exception as err:
            logging.error(f"Failed to check if element {locator} is displayed.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def is_element_hidden(self, locator):
        try:
            element = self.find_element(locator)
            is_displayed = element.is_displayed()
            if not is_displayed:
                logging.info(f"Element {locator} is hidden.")
            else:
                logging.info(f"Element {locator} is not hidden.")
            return not is_displayed
        except NoSuchElementException:
            logging.info(f"Element {locator} is hidden.")
            return True
        except Exception as err:
            logging.error(f"An error occurred while checking if element {locator} is hidden.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def send_text_and_press_enter(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
            logging.info(f"Entered text '{text}' and pressed Enter.")
        except Exception as err:
            logging.error(f"Failed to enter text '{text}' and press Enter.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def send_text_and_press_tab(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.TAB)
            logging.info(f"Entered text '{text}' and pressed Tab.")
        except Exception as err:
            logging.error(f"Failed to enter text '{text}' and press Tab.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    # Handle JavaScript Alerts:
    def handle_alert_js(self, action="accept"):
        try:
            alert = self.driver.switch_to.alert
            if action == "accept":
                alert.accept()
                logging.info("Accepted the alert.")
            elif action == "dismiss":
                alert.dismiss()
                logging.info("Dismissed the alert.")
            else:
                logging.warning("Invalid action provided. Expected 'accept' or 'dismiss'.")
        except Exception as err:
            logging.error("Failed to handle the alert.")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)
