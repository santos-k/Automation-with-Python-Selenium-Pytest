from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
act = ActionChains(driver)

time.sleep(3)
driver.find_element(By.NAME, "q").send_keys("Selenium Python Documentation")
time.sleep(3)

# Press the Enter key
act.send_keys(Keys.ENTER).perform()

time.sleep(3)

# Press Tab key multiple times
for i in range(40):
    if i > 25:
        time.sleep(1)
    act.send_keys(Keys.TAB).perform()
    i += 1

time.sleep(5)
driver.quit()
