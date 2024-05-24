import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        return driver

    elif browser == "Firefox":
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Edge()
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("browser")
