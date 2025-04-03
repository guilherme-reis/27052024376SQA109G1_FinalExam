import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_registration(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 10)

    if "automationexercise" not in driver.title.lower():
        driver.refresh()

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("Test User")
    email = f"testuser{random.randint(1000000, 9999999)}@example.com"
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    assert "Enter Account Information" in driver.page_source
