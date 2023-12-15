from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

act = ActionChains(driver)
act.drag_and_drop(source,target).perform()

time.sleep(5)
driver.quit()
