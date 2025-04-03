import pytest
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
def test_user_registration(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 15)

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("Test User")
    email = f"testuser{random.randint(1000000, 9999999)}@example.com"
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("123456")
    driver.find_element(By.ID, "days").send_keys("1")
    driver.find_element(By.ID, "months").send_keys("January")
    driver.find_element(By.ID, "years").send_keys("2000")
    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "address1").send_keys("123 Test St")
    driver.find_element(By.ID, "state").send_keys("BC")
    driver.find_element(By.ID, "city").send_keys("Vancouver")
    driver.find_element(By.ID, "zipcode").send_keys("V6B1B1")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")
    driver.find_element(By.ID, "country").send_keys("Canada")

    create_btn = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
    driver.execute_script("arguments[0].scrollIntoView();", create_btn)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))).click()

    with open("test_user.txt", "w") as f:
        f.write(email)
