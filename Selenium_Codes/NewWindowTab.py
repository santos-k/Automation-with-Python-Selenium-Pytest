import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Websites url
nopcom = "https://demo.nopcommerce.com/"
fb = "https://www.facebook.com/"
google = "https://www.google.com/"
testauto = "https://testautomationpractice.blogspot.com/"

options = Options()
# options.add_argument("--headless") # this is must for taking entire page screenshot
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get(nopcom)

time.sleep(2)
driver.switch_to.new_window("tab") # open new tab
time.sleep(2)
driver.get(google) # open this url in newly opened tab

time.sleep(2)
driver.switch_to.new_window("window") # open new window
time.sleep(2)
driver.get(fb) # open this url in newly opened window

time.sleep(2)
driver.switch_to.new_window("tab") # this new tab will be opened in previous window, not in new window
time.sleep(2)
driver.get(testauto) # this url will be opened in above tab

for i in driver.window_handles:
    driver.switch_to.window(i)
    print("Title: ", driver.title, "ID: ", i)

print("Current Tab title: ", driver.title)

time.sleep(3)
driver.quit()
