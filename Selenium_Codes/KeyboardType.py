import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Locate the input field
input_field = driver.find_element(By.ID, "textarea")

time.sleep(3)
# scrolling to the textarea element
driver.execute_script("arguments[0].scrollIntoView();", input_field)

time.sleep(3)
# Type text into the input field
input_field.send_keys("Hello, Selenium!")

time.sleep(5)
driver.quit()
