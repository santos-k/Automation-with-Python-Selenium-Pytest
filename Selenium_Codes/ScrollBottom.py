from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")

time.sleep(3)
# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(4)
# Scroll to the Top of the page
driver.execute_script("window.scrollTo(0, 0);")

time.sleep(5)
driver.quit()
