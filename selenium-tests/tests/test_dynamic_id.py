# file intended for test dynamic id

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_dynamic_id():
	# Set Chrome optionen
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode
    chrome_options.add_argument("--no-sandbox")  # Sandbox deaktivation
    chrome_options.add_argument("--disable-dev-shm-usage")  # Shared memory usage deaktivation

    # Selenium Manager wird automatisch den passenden Chromedriver finden
    driver = webdriver.Chrome(options=chrome_options)

    # WebDriver creation
  #   service = Service()  # Optional, falls du einen spezifischen Pfad für den ChromeDriver benötigst
   #  driver = webdriver.Chrome(service=service, options=chrome_options)
	
	# Testlogik
	try: 
		driver.get("http://uitestingplayground.com/dynamicid")
		
		# Look for a Button with a dynamic ID
		button = driver.find_element(By.XPATH, "//button[contains(text(),'Button')]")
		assert button is not None, "Button nicht gefunden"
		button.click()
		# Optional: Validierung nach dem Klick (wenn notwendig)
        # e.g., prüfen, ob eine neue Seite geladen wurde
        # new_element = driver.find_element(By.ID, "expectedElementId")
        # assert new_element is not None, "Expected element not found after click"
	finally:
		# Teardown: Driver schließen, selbst bei Fehlern
		driver.quit()
