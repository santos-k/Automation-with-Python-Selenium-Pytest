import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

# Static Dropdowns
static_dropdown = driver.find_element(By.ID, "dropdown-class-example")
select = Select(static_dropdown)
select.select_by_index(1) # method 1: first value from dropdown
time.sleep(1)
select.select_by_value("option2")  # method 2: Value attribute value
time.sleep(1)
select.select_by_visible_text("Option3")  # method 3: text of dropdown

time.sleep(1)
# Selecting using XPATH
driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']//option[@value='option1']").click()

time.sleep(5)
driver.quit()
