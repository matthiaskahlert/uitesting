# file intended for test dynamic id

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_dynamic_id():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/dynamicid")
    
    # Suche einen Button mit dynamischer ID
    button = driver.find_element(By.XPATH, "//button[contains(text(),'Button')]")
    assert button is not None, "Button nicht gefunden"
    button.click()
    driver.quit()
