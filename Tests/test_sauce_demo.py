import allure
import pytest

from Config import config_data
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

    @allure.title("TC006: Add item to the cart")
    @pytest.mark.module_login
    @pytest.mark.parametrize("username,password", get_data("login_details.csv"))
    def test_add_item_to_the_cart(self, username, password):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_bagpack_count()
        self.product_page.add_bagpack_to_cart()

    @allure.title("TC007: Add item to the cart after clicking on product")
    @pytest.mark.module_login
    @pytest.mark.parametrize("username,password, product_name", get_data("product_name.csv"))
    def test_add_item_to_the_cart_from_product(self, username, password, product_name):
        self.search_page = SauceDemoPage(self.driver)
        self.product_page = SauceDemoProductPage(self.driver)
        self.search_page.navigate_to_page(config_data.url)
        self.search_page.login_to_page(username, password)
        self.product_page.initial_bagpack_count()
        self.product_page.add_product_to_cart(product_name)
