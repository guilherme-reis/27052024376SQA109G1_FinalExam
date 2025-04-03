import pytest
import undetected_chromedriver as uc
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = uc.ChromeOptions()
        driver = uc.Chrome(options=options)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()
