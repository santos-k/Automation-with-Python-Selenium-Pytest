from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.reduceimages.com/")

# Scroll down the page (adjust the range and step based on your needs)
for scroll in range(0, 1000, 200):
    driver.execute_script(f"window.scrollTo(0, {scroll});")
    time.sleep(1)  # Add a short delay to allow the page to render

    # Take a screenshot at each scroll position
    driver.save_screenshot(f"screenshot_scroll_{scroll}.png")

driver.quit()
