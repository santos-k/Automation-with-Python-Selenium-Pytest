# Basic use of Explicit Wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

mywait = WebDriverWait(driver, 10)  # Explicit wait declaration

driver.get("https://www.google.com/")

search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium")
search.submit()

# use of explicit wait
search_link = mywait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'selenium.dev')]//h3")))
search_link.click()


# 2nd use of explicit wait
open_link = mywait.until(EC.presence_of_element_located((By.CLASS_NAME, "selenium-webdriver")))
print(open_link.text)

driver.quit()
