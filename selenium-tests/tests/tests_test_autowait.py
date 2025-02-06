import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_auto_wait():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/autowait")

    # Locate the start button and click it
    start_button = driver.find_element(By.ID, "startButton")
    start_button.click()

    # Wait for the hello text to be displayed
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    # Verify the hello text
    hello_text = driver.find_element(By.ID, "finish").text
    assert hello_text == "Hello World!"

    driver.quit()

if __name__ == "__main__":
    test_auto_wait()