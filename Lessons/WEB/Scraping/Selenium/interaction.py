from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# time.sleep(3)

# Locate the article count link and print its text
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# Locate the "Content portals" link
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# Uncomment the following line if you want to click the link
# all_portals.click()

# Locate the search input field and enter "Python"
search = driver.find_element(By.CLASS_NAME, 'cdx-text-input__input')
search.send_keys("Python", Keys.ENTER)

# Close the browser (remove this line if you want to keep it open)
driver.quit()
