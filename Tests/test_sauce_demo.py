import allure
import pytest

from Config import config_data
from Pages.SauceDemoCart_Page import SauceDemoCartPage
from Pages.SauceDemoHome_Page import SauceDemoPage
from Pages.SauceDemoProduct_Page import SauceDemoProductPage
from Tests.test_base import BaseTest
from Config.config_util import get_data


class TestSauceDemo(BaseTest):
    @allure.title("TC001: Valid login with correct credentials")
    @pytest.mark.module_login
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_sauce_demo_valid_login(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)

    @allure.title("TC002: Login with an invalid username")
    @pytest.mark.module_login
    @pytest.mark.parametrize("username,password", get_data("Invalidloginusername_details.csv"))
    def test_sauce_demo_invalid_username(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page_with_invalid_username_password(username, password)

    @allure.title("TC003: Login with an invalid password")
    @pytest.mark.module_login
    @pytest.mark.parametrize("username,password", get_data("Invalidloginpassword_details.csv"))
    def test_sauce_demo_invalid_password(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page_with_invalid_username_password(username, password)

    @allure.title("TC004: Login with both invalid username and password")
    @pytest.mark.module_login
    @pytest.mark.parametrize("username,password", get_data("Invalidlogin_details.csv"))
    def test_sauce_demo_invalid_username_password(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page_with_invalid_username_password(username, password)

    @allure.title("TC005: Valid login with correct credentials and logout")
    @pytest.mark.module_login
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_sauce_demo_login_and_logout(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.search_page.logout_of_page()

    @allure.title("TC006: Cart is empty when a user logs in")
    @pytest.mark.module_cart
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_add_item_to_the_cart_from_product(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.check_cart_is_empty()

    @allure.title("TC007: Add item to the cart from product page")
    @pytest.mark.module_cart
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_add_item_to_the_cart(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_bagpack_to_cart()

    @allure.title("TC008: Add item to the cart after clicking on product")
    @pytest.mark.module_cart
    @pytest.mark.parametrize("username,password, product_name", get_data("product_name.csv"))
    def test_add_item_to_the_cart_from_product(self, username, password, product_name):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_product_to_cart(product_name)

    @allure.title("TC009: Add more than one product in cart from product page")
    @pytest.mark.module_cart
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_add_multiple_item_to_the_cart_from_product_page(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_two_products_to_cart()
        self.product_page.verify_products_in_cart()

    @allure.title("TC010: Product should be present which user added before logging out")
    @pytest.mark.module_cart
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_product_check_after_logout(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_two_products_to_cart()
        self.product_page.verify_products_in_cart()
        self.search_page.logout_of_page()
        self.search_page.login_to_page(username, password)
        self.product_page.verify_products_in_cart()

    @allure.title("TC011: Remove item from the cart from product page")
    @pytest.mark.module_cart
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_remove_item_from_product_page(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_two_products_to_cart()
        self.product_page.verify_products_in_cart()
        self.product_page.continue_shopping()
        self.product_page.remove_two_products_to_cart()
        self.product_page.check_cart_is_empty()

    @allure.title("TC012: Remove item from the cart")
    @pytest.mark.module_cart
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_remove_item_from_cart(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_two_products_to_cart()
        self.product_page.verify_products_in_cart()
        self.product_page.remove_two_products_to_cart()

    @allure.title("TC013: Cart is empty after removing all items")
    @pytest.mark.module_cart
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_check_cart_is_empty_after_removing_all(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_two_products_to_cart()
        self.product_page.verify_products_in_cart()
        self.product_page.remove_two_products_to_cart()
        self.product_page.check_cart_is_empty()

    @allure.title("TC014: Successful checkout with valid information")
    @pytest.mark.module_checkout
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_checkout_with_valid_details(self, username, password, first_name="Harshit", last_name="Sinha",
                                         zipcode="41089"):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.checkout_page = SauceDemoCartPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_two_products_to_cart()
        self.product_page.verify_products_in_cart()
        self.checkout_page.click_on_checkout()
        self.checkout_page.enter_valid_shipping_details(first_name, last_name, zipcode)
        self.checkout_page.verify_products_while_checkout()
        self.checkout_page.place_order_and_verify()

    @allure.title("TC015: Checkout without entering shipping information")
    @pytest.mark.module_checkout
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_checkout_with_invalid_details(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.checkout_page = SauceDemoCartPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.add_two_products_to_cart()
        self.product_page.verify_products_in_cart()
        self.checkout_page.click_on_checkout()
        self.checkout_page.click_on_continue_without_any_details()

    @allure.title("TC016: Checkout with an empty cart")
    @pytest.mark.module_checkout
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_checkout_with_empty_cart(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.checkout_page = SauceDemoCartPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_cart_count()
        self.product_page.check_cart_is_empty()
        self.checkout_page.click_on_continue_with_empty_cart()

