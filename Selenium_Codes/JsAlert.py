from selenium import webdriver
from selenium.webdriver.common.by import By
import time

heroku = "https://the-internet.herokuapp.com/"
driver = webdriver.Chrome()
driver.get(heroku)
driver.maximize_window()

# Opening Alert page
driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()


# Switch to the alert
alert = driver.switch_to.alert

# Get the text of the alert
alert_text = alert.text
print("Alert Text:", alert_text)

time.sleep(2)
# Accept the alert (click OK)
alert.accept()

# Dismiss the alert (click Cancel)
# alert.dismiss()

# switch driver focus to html page/ default
driver.switch_to.default_content()
print("Result: ", driver.find_element(By.ID, "result").text)

time.sleep(2)
driver.quit()
