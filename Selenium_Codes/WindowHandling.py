from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)

wiki = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
wiki.send_keys("Cricket")
wiki.submit()

# Opening new window tabs using the attribute target="_blank"
wiki_links = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']//a")
for link in wiki_links:
    link.click()

# printing id of current tab
current_window_id = driver.current_window_handle
print("Id of current window: ", current_window_id)

# Id of all opened tabs
all_opened_windows = driver.window_handles
print("List of All Opened Windows ID: ", all_opened_windows)

# switching windows and printing title with window id
for i in all_opened_windows:
    driver.switch_to.window(i)
    print(f"Window Tab Title: {driver.title.ljust(30)}, Window ID: {i}")

# switching driver to first window
driver.switch_to.window(all_opened_windows[0])

# confirm the title of first window
print("Current Window Title: ", driver.title)

# window close
# driver.close () # close current window only
# driver.quit() # close all windows at once

for i in all_opened_windows:
    driver.switch_to.window(i)
    print(f"{driver.title.ljust(30)} : Closed")
    driver.close()
    time.sleep(2)

time.sleep(3)
driver.quit()
