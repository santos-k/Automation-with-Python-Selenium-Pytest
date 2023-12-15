from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://skill-test.net/mouse-double-click")

act = ActionChains(driver)
double_click_it = driver.find_element(By.ID, "clicker")

act.double_click(double_click_it).perform()

time.sleep(4)
driver.quit()
