import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Add below four lines of code disable auto close of Chrome browser
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)

# Open Chrome
driver = webdriver.Chrome(options=options)  # Open Chrome
driver.maximize_window()  # Maximize the window

# Open URL
# url = "https://rahulshettyacademy.com/AutomationPractice/"
url = "https://www.saucedemo.com/"
driver.get(url)  # open this url
title = driver.title
if title == "Swag Labs":
    print("Title text Pass")
else:
    print("Title text Fail")
login_container_msg = driver.find_element(By.CLASS_NAME, "login_logo").text
if login_container_msg == "Swag Labs":
    print("Login Page Heading text  Pass")
else:
    print("Login Page Heading text Fail")

username_placeholder = driver.find_element(By.ID, "user-name").get_attribute("placeholder")
if username_placeholder == "Username":
    print("Username input placeholder text Pass")
else:
    print("Username placeholder text Fail")

password_placeholder = driver.find_element(By.ID, "password").get_attribute("placeholder")
if password_placeholder == "Password":
    print("Password input placeholder text Pass")
else:
    print("Password input placeholder text Fail")

login_btn_name = driver.find_element(By.ID, "login-button").get_attribute("value")
if login_btn_name == "Login":
    print("Login button text Pass")
else:
    print("Login button text Fail")

accepted_users = driver.find_element(By.CLASS_NAME,'login_credentials').text.split("\n")[1:]
if len(accepted_users) == 6:
    print("Accepted no of users Pass")
else:
    print("Accepted no of users Fail")

accepted_password = driver.find_element(By.CLASS_NAME,'login_password').text.split("\n")[1:]
if len(accepted_password) == 1:
    print("Accepted no of Password Pass")
else:
    print("Accepted no of Password Fail")


# Testing Username required error
driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, 'password').clear()
driver.find_element(By.ID, 'login-button').click()
error_msg = driver.find_element(By.XPATH, "//div[@class='login-box']//div[starts-with(@class,'error-message')]").text
if error_msg == "Epic sadface: Username is required":
    print("Username is required: Pass")
else:
    print("Username is required: Fail")

# Testing Password required error
driver.find_element(By.ID, "user-name").send_keys("abc")
driver.find_element(By.ID, 'password').clear()
driver.find_element(By.ID, 'login-button').click()
error_msg = driver.find_element(By.XPATH, "//div[@class='login-box']//div[starts-with(@class,'error-message')]").text
if error_msg == "Epic sadface: Password is required":
    print("Password is required: Pass")
else:
    print("Password is required: Fail")


# Test wrong username or password scenarios
driver.find_element(By.ID, "user-name").send_keys('abc')
driver.find_element(By.ID, 'password').send_keys(accepted_password[0])
driver.find_element(By.ID, 'login-button').click()
error_msg = driver.find_element(By.XPATH, "//div[@class='login-box']//div[starts-with(@class,'error-message')]").text
if error_msg == "Epic sadface: Username and password do not match any user in this service":
    print("Username and password do not match: Pass")
else:
    print("Username and password do not match: Fail")

# Test Login Scenarios with correct data
try:
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(accepted_users[0])
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(accepted_password[0])
    driver.find_element(By.ID, "login-button").click()
    print("Successfully Login: Pass")
except Exception:
    print("Successfully Login: Fail")

time.sleep(10)
driver.quit()

