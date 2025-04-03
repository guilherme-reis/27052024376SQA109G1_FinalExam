import pytest
import undetected_chromedriver as uc

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = uc.Chrome(options=options)
    else:
        from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver
        driver = SafariDriver()

    yield driver
    driver.quit()
