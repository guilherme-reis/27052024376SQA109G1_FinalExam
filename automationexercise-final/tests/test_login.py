import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
def test_user_login(driver, request):
    browser = request.config.getoption("--browser")
    with open(f"test_user_{browser}.txt", "r") as f:
        email = f.read().strip()

    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 15)

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

    user_tag = wait.until(
        EC.presence_of_element_located((By.XPATH, "//li/a[contains(text(),'Logged in as')]"))
    )

    assert user_tag.is_displayed()
