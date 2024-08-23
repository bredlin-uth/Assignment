import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from generic_utils import Common_Utils


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Invalid Browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Common_Utils.get_config("basic info", "url"))
    request.cls.driver = driver
    yield
    driver.quit()
