from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Navigate to a webpage
driver.get("https://www.reduceimages.com/")

time.sleep(5)
# Take a screenshot of the entire page
driver.save_screenshot("full_page_screenshot2.png")
print("saved")

# Close the browser
driver.quit()
