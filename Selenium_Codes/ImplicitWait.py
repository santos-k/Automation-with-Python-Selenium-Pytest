from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# Set implicit wait to 10 seconds, it declares only once at top
# Now, any subsequent element lookups will wait up to 10 seconds before raising a NoSuchElementException

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

text = driver.find_element(By.ID, "autocomplete")
text.send_keys("Hello, Rohit!")
print(text.get_attribute("value"))

driver.quit()
