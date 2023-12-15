# Scroll down to element position
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.orangehrm.com/")

time.sleep(3)
target = driver.find_element(By.XPATH, "//div[@class='homepage-product-content ']//h2")
driver.execute_script("arguments[0].scrollIntoView();", target) # scroll to element

time.sleep(5)
driver.quit()
