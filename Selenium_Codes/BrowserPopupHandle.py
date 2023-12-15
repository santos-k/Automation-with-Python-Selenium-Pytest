from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--incognito")
# options.add_argument("--disable-notifications")
options.add_argument("--window-size=1000,800")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
# driver.maximize_window()

driver.get("https://whatmylocation.com/")
print(driver.title)
time.sleep(5)
driver.quit()
