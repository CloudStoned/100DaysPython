from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

gforms_url = "https://forms.gle/fTfDy9RJxLMvMkvk9"
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def get_details(url):
    try:
        print("GETTING DETAILS...")
        driver.get(url)
        driver.implicitly_wait(10)

        property_cards = driver.find_elements(By.CLASS_NAME, 'property-card-link')
        property_prices = driver.find_elements(By.CLASS_NAME, 'PropertyCardWrapper__StyledPriceLine')
        property_addresses = driver.find_elements(By.CSS_SELECTOR, '[data-test="property-card-addr"]')

        property_links = [card.get_attribute('href') for card in property_cards]
        property_prices = [f"${re.sub(r'[^\d]', '', price.text)}" for price in property_prices]
        property_addresses = [address.text.replace('|', '').replace('\n', '').strip() for address in property_addresses]

    except Exception as e:
        print(f"An error occurred while getting details: {e}")
        property_links, property_prices, property_addresses = [], [], []

    return property_links, property_prices, property_addresses

def write_in_forms(url, links, prices, addresses):
    print("WRITING IN FORMS...")
    driver.get(url)
    wait = WebDriverWait(driver, 60)  # Increased wait time

    for i in range(len(links)):
        try:
            address_input = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
            )
            price_input = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
            )
            link_input = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
            )
            submit_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
            )
            
            address_input.clear()
            address_input.send_keys(addresses[i])
            
            price_input.clear()
            price_input.send_keys(prices[i])
            
            link_input.clear()
            link_input.send_keys(links[i])
            
            submit_button.click()
            
            # Wait for the resubmit button and click it
            resubmit_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))
            )
            resubmit_button.click()
            
            print(f"Submission {i + 1} completed.")

        except Exception as e:
            print(f"An error occurred during form submission {i + 1}: {e}")

        time.sleep(2)  # Add a brief delay to avoid overwhelming the server

    print("All submissions completed.")

links, prices, addresses = get_details(zillow_url)
write_in_forms(gforms_url, links, prices, addresses)

driver.quit()
