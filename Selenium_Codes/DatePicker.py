from selenium import webdriver
from selenium.webdriver.common.by import By
import time

testauto = "https://testautomationpractice.blogspot.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(testauto)

iframe = driver.find_element(By.ID, "frame-one796456169")

driver.switch_to.frame(iframe)

# date element
date = driver.find_element(By.ID, "RESULT_TextField-2")
print(type(date.text), date.text)
print(date.get_attribute("placeholder"))

time.sleep(5)
date.send_keys("09/12/2023")
time.sleep(2)
print(date.get_attribute("value"))
date.clear()
time.sleep(2)
date.send_keys("11/09/2020")
time.sleep(2)
print(date.get_attribute("value"))
date.clear()

time.sleep(4)
driver.quit()
