from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Create a webdriver instance (e.g., Chrome)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Navigate to a webpage
driver.get("https://www.reduceimages.com/")

time.sleep(5)

# take a screenshot of a specific element
#  = driver.find_element(By.XPATH, "//*[@id='how-it-works']/div/div/div[1]/div[1]/div/div[2]/div/h3")
element = driver.find_element(By.XPATH, "//*[@id='how-it-works']/div/div/div[1]/div[1]/div/div[1]/img")
element.screenshot("element_screenshot.png")

print("Saved")
driver.quit()
