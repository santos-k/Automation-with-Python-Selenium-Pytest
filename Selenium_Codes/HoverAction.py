from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")

main_menu = driver.find_element(By.CLASS_NAME, "header-main__list-item")
sub_menu = driver.find_element(By.XPATH, "/html/body/nav/div/div[1]/ul[1]/li[1]/ul/li[2]/span")
item = driver.find_element(By.XPATH, "/html/body/nav/div/div[1]/ul[1]/li[1]/ul/li[2]/ul/li[3]/a")

time.sleep(2) # just to see the action

# Hover actions, 3 moves
act = ActionChains(driver)
act.move_to_element(main_menu).move_to_element(sub_menu).move_to_element(item).click().perform()

time.sleep(3)
driver.quit()
