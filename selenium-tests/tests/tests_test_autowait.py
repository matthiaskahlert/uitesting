import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_auto_wait():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/autowait")

    # Step 2: Click the applyButton5
    apply_button = driver.find_element(By.ID, "applyButton5")
    apply_button.click()

    # Step 3: Wait for five seconds
    time.sleep(5)

    # Step 4: Click the button with the ID target
    target_button = driver.find_element(By.ID, "target")
    target_button.click()

    # Step 5: Validate the text "Target clicked."
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "target"), "Target clicked.")
    )
    target_text = driver.find_element(By.ID, "target").text
    assert target_text == "Target clicked."

    driver.quit()

if __name__ == "__main__":
    test_auto_wait()