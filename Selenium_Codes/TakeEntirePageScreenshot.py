# Entire Page Screenshot
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")  # this is must for taking entire page screenshot
driver = webdriver.Chrome(options=options)
driver.maximize_window()

URL = "https://www.reduceimages.com/"
driver.get(URL)

width = 1920
height = driver.execute_script(
    "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
print(width, height)

driver.set_window_size(width, height)
full_page = driver.find_element(By.TAG_NAME, "body")

full_page.screenshot("Entire_Page_Screenshot.png")
print("Saved")
time.sleep(3)
driver.quit()
