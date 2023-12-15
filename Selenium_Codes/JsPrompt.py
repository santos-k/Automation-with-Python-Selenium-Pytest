from selenium import webdriver
from selenium.webdriver.common.by import By
import time

heroku = "https://the-internet.herokuapp.com/"
driver = webdriver.Chrome()
driver.get(heroku)
driver.maximize_window()

# Opening Alert page
driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()

# Switch to the prompt
prompt = driver.switch_to.alert

# Get the text of the prompt
prompt_text = prompt.text
print("Prompt Text:", prompt_text)

time.sleep(2)
# Enter text into the prompt
prompt.send_keys("Selenium is awesome!")

# Accept the prompt (click OK)
prompt.accept()

# Dismiss the prompt (click Cancel)
# prompt.dismiss()

# switch driver focus to html page/ default
driver.switch_to.default_content()
print("Result: ", driver.find_element(By.ID, "result").text)

time.sleep(2)
driver.quit()
