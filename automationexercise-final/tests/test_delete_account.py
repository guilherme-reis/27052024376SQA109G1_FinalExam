import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
def test_delete_account(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 15)

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    with open("test_user.txt", "r") as f:
        email = f.read().strip()

    wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete Account"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//b[text()='Account Deleted!']")))
