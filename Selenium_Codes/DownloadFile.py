from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
opt.add_argument("--disable-popup-blocking")
opt.add_experimental_option('detach', True)
opt.add_experimental_option('prefs', {"safebrowsing.enabled": 1})

# Add preferences to enable or disable safe browsing
# 0: Safe Browsing disabled, 1: Safe Browsing enabled

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get("https://www.sublimetext.com/download")
driver.maximize_window()

act = ActionChains(driver)

time.sleep(3)

download_file = driver.find_element(By.XPATH, "//*[@id='dl_win_64']/a[1]")
download_file.click()

time.sleep(10)
driver.quit()
