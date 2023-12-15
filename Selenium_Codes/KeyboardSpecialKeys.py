from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

act = ActionChains(driver)

time.sleep(3)
driver.find_element(By.NAME, "q").send_keys("Selenium Python Documentation")

time.sleep(3)

# Press the Enter key
act.send_keys(Keys.ENTER).perform()

time.sleep(3)

# press Down_Arrow key 5 times
for i in range(5):
    time.sleep(2)
    act.send_keys(Keys.ARROW_DOWN).perform()
    i += 1

# press Up_Arrow key 5 times
for i in range(5):
    time.sleep(2)
    act.send_keys(Keys.ARROW_UP).perform()
    i += 1

# press PageUP key 5 times
for i in range(5):
    time.sleep(2)
    act.send_keys(Keys.PAGE_DOWN).perform()
    i += 1

# press PageDown key 5 times
for i in range(5):
    time.sleep(2)
    act.send_keys(Keys.PAGE_DOWN).perform()
    i += 1

# press Home key 5 times
for i in range(5):
    time.sleep(2)
    act.send_keys(Keys.HOME).perform()
    i += 1

# press END key 5 times
for i in range(5):
    time.sleep(2)
    act.send_keys(Keys.END).perform()
    i += 1


time.sleep(3)
driver.quit()
