from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("TestingFname")

fname = driver.find_element(By.NAME, "lName")
fname.send_keys("TestingLname")

fname = driver.find_element(By.NAME, "email")
fname.send_keys("EmailTesting@gmail.com")

btn_signup = driver.find_element(By.CSS_SELECTOR, "form button")
btn_signup.click()

