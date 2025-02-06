# file intended for test autowait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Testlogik

def test_auto_wait():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/autowait")


    try:
        # Step 2: Warte auf den Apply-Button und klicke ihn
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "applyButton5"))
        )
        apply_button.click()

        # Step 3: Warte auf das Erscheinen des Target-Buttons
        target_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "target"))
        )
        target_button.click()

        # Step 5: Validieren des Texts "Target clicked."
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "target"), "Target clicked.")
        )
        target_text = driver.find_element(By.ID, "target").text
        assert target_text == "Target clicked.", f"Test Failed: Expected 'Target clicked.', got '{target_text}'"
        print("Test Passed: Target text is 'Target clicked.'")
    
    except Exception as e:
        print(f"Test Failed: {str(e)}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_auto_wait()