import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_user_registration(driver):
    driver.get("https://automationexercise.com/")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    driver.find_element(By.NAME, "name").send_keys("Test User")
    email = f"testuser{random.randint(1000,9999)}@example.com"
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    time.sleep(3)
    assert "Enter Account Information" in driver.page_source
