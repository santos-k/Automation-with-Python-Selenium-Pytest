from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()

act = ActionChains(driver)

time.sleep(3)
driver.find_element(By.NAME, "q").send_keys("Selenium Python Documentation")

time.sleep(3)

# Press the Enter key
act.send_keys(Keys.ENTER).perform()

time.sleep(3)

# Combining keys (pressing Ctrl+A to select all text)
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

time.sleep(2)
# Combining keys (pressing Ctrl+C to select all text)
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

time.sleep(2)
driver.get("https://www.rapidtables.com/tools/notepad.html")

time.sleep(2)
text_area = driver.find_element(By.ID, "area")
text_area.send_keys("Written by Selenium: ")
print(text_area.get_attribute("class"))

time.sleep(2)
# Paste : Ctrl + V
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(5)
driver.quit()
