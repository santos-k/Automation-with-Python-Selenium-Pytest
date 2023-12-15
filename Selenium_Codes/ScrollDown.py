from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")

# Scroll down by a certain number of pixels (e.g., 500)
# driver.execute_script(f"window.scrollBy(0, 500);")

for i in range(0, 10):
    driver.execute_script(f"window.scrollBy(0, {10 * i});")
    value = driver.execute_script("return window.pageYOffset;")
    print("No of Pixels moved: ", value)
    time.sleep(2)

time.sleep(5)
driver.quit()
