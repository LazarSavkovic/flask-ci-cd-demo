import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Default to your Render URL; override with BASE_URL in CI if needed
BASE_URL = os.getenv(
    "BASE_URL",
    "https://flask-ci-cd-demo-latest.onrender.com"
)


def test_alert_button_triggers_alert():
    # Headless Chrome options (works in CI runners)
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(BASE_URL + "/")

        # Wait until button is clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "alert-btn"))
        )
        button.click()

        # Wait for JS alert to appear
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert

        assert alert.text == "Hello from CI/CD frontend!"
        alert.accept()
    finally:
        driver.quit()
