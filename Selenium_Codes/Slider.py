from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

slider = driver.find_element(By.XPATH, "//div[@id='slider']//span")
print(slider.get_attribute("style"))
print("Location: ", slider.location)
act = ActionChains(driver)

time.sleep(3)
act.drag_and_drop_by_offset(slider, 200, 0).perform()

slider = driver.find_element(By.XPATH, "//div[@id='slider']//span")
print(slider.get_attribute("style"))
print("Location: ", slider.location)

time.sleep(3)
driver.quit()
