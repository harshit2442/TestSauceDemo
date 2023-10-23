import logging
import os

import pytest
from Config import config_data
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service

log = logging.getLogger(__name__)


def pytest_configure(config):
    """Create log file if log file is not mentioned in ini file"""
    if not config.option.log_file:
        config.option.log_file = '../execution.log'
    # Set the logging level to INFO
    logging.basicConfig(level=logging.INFO)


@pytest.fixture(params=[config_data.browser], scope=config_data.driver_scope)
def init_driver(request):
    if request.param == "chrome":
        if not config_data.debug:
            logging.info("\n\n=====starting test(" + request.node.name + ")================")
            yield from initiate_chromedriver(request)
    elif request.param == "firefox":
        initiate_firefoxdriver(request)  # Call the fixture directly without 'yield from'
    elif request.param == "ie":
        initiate_iedriver(request)  # Call the fixture directly without 'yield from'
    elif request.param == "edge":
        initiate_edgedriver(request)  # Call the fixture directly without 'yield from'


def initiate_chromedriver(request):
    chrome_options = webdriver.ChromeOptions()
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()


def initiate_firefoxdriver(request):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    yield
    driver.quit()


def initiate_iedriver(request):
    driver = webdriver.Ie(IEDriverManager().install())
    request.cls.driver = driver
    yield
    driver.quit()


def initiate_edgedriver(request):
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = driver
    yield
    driver.quit()
