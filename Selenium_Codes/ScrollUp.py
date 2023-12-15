from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

time.sleep(3)

# scroll down
driver.execute_script(f"window.scrollBy(0, 500);")
time.sleep(3)

# Scroll up by a certain number of pixels (e.g., -500)
driver.execute_script("window.scrollBy(0, -500);")

time.sleep(5)
driver.quit()
