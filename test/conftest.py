import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Invalid Browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    request.cls.driver = driver
    yield
    driver.quit()
