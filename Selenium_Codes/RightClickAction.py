from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

right_click_btn = driver.find_element(By.CLASS_NAME, "btn-neutral")

# Right click action(context click)
act = ActionChains(driver)
act.context_click(right_click_btn).perform()

time.sleep(2)
clk = driver.find_element(By.CLASS_NAME, "context-menu-icon-edit")

# single click
act.click(clk).perform()

time.sleep(3)
driver.quit()
