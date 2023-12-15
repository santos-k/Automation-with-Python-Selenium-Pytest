from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
# opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# opt.add_argument("--disable-popup-blocking")
opt.add_experimental_option('detach', True)
opt.add_experimental_option('prefs', {"safebrowsing.enabled": 1})

driver = webdriver.Chrome(options=opt)
driver.get("https://imageresizer.com/")


# Locate the file input element
file_input = driver.find_element(By.ID, "file-input")

# Provide the path to the file you want to upload
file_path = "C:/Selenium/Projects/img_10.png"
file_input.send_keys(file_path)
print("File uploaded")

# Perform other actions as needed
time.sleep(10)
driver.quit()
