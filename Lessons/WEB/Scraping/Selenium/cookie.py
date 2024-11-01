from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the language selection button to be clickable and click it
try:
    wait = WebDriverWait(driver, 10)
    lang = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
    lang.click()

    # Wait for the cookie to be clickable
    cookie = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cookieAnchor button")))
    
    # Click the cookie
    while True:
        cookie.click()
        cookie.click()
        time.sleep(0.1)  
finally:
    # Optionally, you can close the WebDriver after some time or based on a condition
    # driver.quit()
    pass
