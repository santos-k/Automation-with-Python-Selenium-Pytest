import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.facebook.com/")

# print(f"Page Title: {driver.title}")
# current_link = driver.current_url
# print(f"Current URL: {current_link}")
#
# # Logo
# logo_displayed = driver.find_element(By.CLASS_NAME, "fb_logo").is_displayed()
# print("Logo Displayed Case: ", "Pass" if logo_displayed == True else "Fail")
#
# # Caption
# caption = driver.find_element(By.CLASS_NAME, "_8eso").is_displayed()
# print(f"Caption Displayed case: ", "Pass" if caption == True else "Fail")
#
# # Caption Text
# caption_text = driver.find_element(By.CLASS_NAME, "_8eso").text
# print(f"Caption Text match case: ", "Pass" if caption_text == "Facebook helps you connect and share with the people in your life." else "Fail")
#
# # Login Form
# form = driver.find_element(By.CLASS_NAME, "_9vtf").is_displayed()
# print(f"Login Form Displayed: ", "Pass" if form == True else "Fail")
#
# # Email input
# email = driver.find_element(By.ID, "email").is_displayed()
# print(f"Email input displayed: ", "Pass" if email == True else "Fail")
#
# # Check Email input is enabled
# email_enabled = driver.find_element(By.ID, "email").is_enabled()
# print("Email input is enabled: ", "Pass" if email_enabled == True else "Fail")
#
# # Email placeholder
# email_placeholder = driver.find_element(By.ID, "email").get_attribute("placeholder")
# print("Email Placeholder as expected: ", "Pass" if email_placeholder == "Email address or phone number" else "Fail")
#
# # Password Input
# password = driver.find_element(By.ID, "pass").is_displayed()
# print(f"Password input displayed: ", "Pass" if password == True else "Fail")
#
# # Check Password input is enabled
# pass_enabled = driver.find_element(By.ID, "pass").is_enabled()
# print("Password input is enabled: ", "Pass" if pass_enabled == True else "Fail")
#
# # Password placeholder
# password_placeholder = driver.find_element(By.ID, "pass").get_attribute("placeholder")
# print("Password Placeholder as expected: ", "Pass" if password_placeholder == "Password" else "Fail")
#
# # Check login Button
# login_button = driver.find_element(By.NAME, "login").tag_name
# print("Login Button is a button: ", "Pass" if login_button == "button" else "Fail")
#
# # Check login btn is displayed
# login_button_display = driver.find_element(By.NAME, "login").is_displayed()
# print("Login Button is displayed: ", "Pass" if login_button_display == True else "Fail")
#
# # Check login btn is enabled
# login_button_enabled = driver.find_element(By.NAME, "login").is_enabled()
# print("Login Button is enabled: ", "Pass" if login_button_enabled == True else "Fail")
#
# # Check login btn text
# login_button_text = driver.find_element(By.NAME, "login").text
# print("Login Button text is as Expected: ", "Pass" if login_button_text == "Log in" else "Fail")
#
# # Forget Password
# forgot_pass_text = driver.find_element(By.CLASS_NAME, "_6ltj").text
# print("Forgot Password Link text as Expected: ", "Pass" if forgot_pass_text == "Forgotten password?" else "Fail")
#
# forgot_pass_tag = driver.find_element(By.XPATH, "//div[@class='_6ltj']//a").tag_name
# print("Forgot Password is a link: ", "Pass" if forgot_pass_tag == 'a' else "Fail")
#
# # Forget password url format
# url_pattern = re.compile(r'^https://www\.facebook\.com/recover/initiate/\?privacy_mutation_token=[\w%=&]+&ars=facebook_login$')
# forget_link = driver.find_element(By.LINK_TEXT, forgot_pass_text).get_attribute("href")
# print("Forget Password link is in a valid format: ", "Pass" if url_pattern.match(forget_link) else "Fail")
#
# # Create Account
# new = driver.find_element(By.LINK_TEXT, "Create new account")
# print("Create New Account is a link: ", "Pass" if new.tag_name == 'a' else 'Fail')
# print("Create New Account text as expected: ", "Pass" if new.text == "Create new account" else "Fail")
# print("Create New Account role as button: ", "Pass" if new.get_attribute("role") == "button" else "Fail")
# print("Create New Account button color as expected: ", "Pass" if new.value_of_css_property("background-color") == "rgba(66, 183, 42, 1)" else "Fail")
#
# # Create a Page
# create_page = driver.find_element(By.ID, "reg_pages_msg")
# print("Create Page text as Expected: ", "Pass" if create_page.text == "Create a Page for a celebrity, brand or business." else "Fail")
#
# # Create Page link
# page_link = driver.find_element(By.CLASS_NAME, "_8esh")
# print("Create a Page has a link", "Pass" if page_link.tag_name == 'a' else "Fail")
#
# # Page Footer
# footer = driver.find_element(By.ID, "pageFooter")
# print("Page has a footer: ", "Pass" if footer.tag_name == "div" else "Fail")
#
# language = driver.find_element(By.CLASS_NAME, "localeSelectorList").text
# print(language.split("\n"))
# print("Expected no of Languages available: ", "Pass" if len(language.split("\n")) == 11 else "Fail")
# print("English (UK) language present: ", "Pass" if "English (UK)" in language.split("\n") else "Fail")
# print("हिन्दी language present: ", "Pass" if "हिन्दी" in language.split("\n") else "Fail")
#
# # Footer Children link
# children = driver.find_elements(By.XPATH, "//div[@id='pageFooterChildren']//ul//li")
# print("Expected no of Child link present: ", "Pass" if len(children) == 31 else "Fail")
#
# # Copyright in footer
# copyright = driver.find_element(By.CLASS_NAME, "copyright")
# print("Copyright available: ", "Pass" if copyright.is_displayed() == True else "Fail")
# print("Copyright text as expected: ", "Pass" if copyright.text == "Meta © 2023" else "Fail")
#
# # Testing Login Form with Data
# email = driver.find_element(By.ID, "email")
# pswd = driver.find_element(By.ID, "pass")
# login_btn = driver.find_element(By.NAME, "login")
#
# # Test Email Error
# email.click()
# pswd.click()
# login_btn.click()
# print("Redirected to new URL: ", "Pass" if driver.current_url != current_link else "Fail")
#
# login_error_img = driver.find_element(By.CLASS_NAME, "_9ay6").tag_name
# print("Login Input Error image present: ", "Pass" if login_error_img == 'img' else "False")
#
# login_error_msg = driver.find_element(By.CLASS_NAME, "_9ay7")
# expected_login_error = "The email address or mobile number you entered isn't connected to an account. Find your account and log in."
# print("Login Error Message as expected: ", "Pass" if login_error_msg == expected_login_error else "Fail")
#
# print("Error Message text color should red: ", "Pass" if login_error_msg.value_of_css_property("color") == "rgba(240, 40, 73, 1)" else "Fail")
# print("Find your account and log in text has a link: ", "Pass" if driver.find_element(By.XPATH, "//div[@class='_9ay7']//a").is_displayed() else "Fail")
#
# # Password Error
# driver.find_element(By.ID, "email").send_keys("salmankhan")
# driver.find_element(By.ID, "pass").send_keys("")
# driver.find_element(By.NAME, "login").click()
# pass_error = driver.find_element(By.CLASS_NAME, "_9ay7").text
# print("Password Error Message without password: ", "Pass" if pass_error == "The password that you've entered is incorrect. Forgotten password?" else "Fail")
#
# # Password Error
# driver.find_element(By.ID, "email").clear()
# driver.find_element(By.ID, "email").send_keys("salmankhan")
# driver.find_element(By.ID, "pass").send_keys("Salmankhan")
# driver.find_element(By.NAME, "login").click()
# pass_error = driver.find_element(By.CLASS_NAME, "_9ay7").text
# print("Password Error Message with incorrect password: ", "Pass" if pass_error == "The password that you've entered is incorrect. Forgotten password?" else "Fail")


# Optimizing about code
def print_result(description, result):
    print(f"{description}: {'Pass' if result else 'Fail'}")


def check_element_displayed(by, value):
    element_displayed = driver.find_element(by, value).is_displayed()
    return element_displayed


def check_element_text(by, value, expected_text):
    element_text = driver.find_element(by, value).text
    return element_text == expected_text


def check_element_attribute(by, value, attribute, expected_value):
    element_attribute = driver.find_element(by, value).get_attribute(attribute)
    return element_attribute == expected_value


def check_url_format(url, pattern):
    return pattern.match(url) is not None


print(f"Page Title: {driver.title}")
current_link = driver.current_url
print(f"Current URL: {current_link}")

# Logo
print_result("Logo Displayed Case", check_element_displayed(By.CLASS_NAME, "fb_logo"))

# Caption
print_result("Caption Displayed case", check_element_displayed(By.CLASS_NAME, "_8eso"))

# Caption Text
print_result("Caption Text match case", check_element_text(By.CLASS_NAME, "_8eso",
                                                           "Facebook helps you connect and share with the people in your life."))

# Login Form
print_result("Login Form Displayed", check_element_displayed(By.CLASS_NAME, "_9vtf"))

# Email input
print_result("Email input displayed", check_element_displayed(By.ID, "email"))
print_result("Email input is enabled", driver.find_element(By.ID, "email").is_enabled())
print_result("Email Placeholder as expected",
             check_element_attribute(By.ID, "email", "placeholder", "Email address or phone number"))

# Password Input
print_result("Password input displayed", check_element_displayed(By.ID, "pass"))
print_result("Password input is enabled", driver.find_element(By.ID, "pass").is_enabled())
print_result("Password Placeholder as expected", check_element_attribute(By.ID, "pass", "placeholder", "Password"))

# Check login Button
print_result("Login Button is a button", driver.find_element(By.NAME, "login").tag_name == "button")
print_result("Login Button is displayed", check_element_displayed(By.NAME, "login"))
print_result("Login Button is enabled", driver.find_element(By.NAME, "login").is_enabled())
print_result("Login Button text is as Expected", check_element_text(By.NAME, "login", "Log in"))

# Forget Password
forgot_pass_text = driver.find_element(By.CLASS_NAME, "_6ltj").text
print_result("Forgot Password Link text as Expected", forgot_pass_text == "Forgotten password?")
print_result("Forgot Password is a link", driver.find_element(By.XPATH, "//div[@class='_6ltj']//a").tag_name == 'a')

# Forget password url format
url_pattern = re.compile(
    r'^https://www\.facebook\.com/recover/initiate/\?privacy_mutation_token=[\w%=&]+&ars=facebook_login$')
forget_link = driver.find_element(By.LINK_TEXT, forgot_pass_text).get_attribute("href")
print_result("Forget Password link is in a valid format", check_url_format(forget_link, url_pattern))

# Create an Account
new = driver.find_element(By.LINK_TEXT, "Create new account")
print_result("Create New Account is a link", new.tag_name == 'a')
print_result("Create New Account text as expected", new.text == "Create new account")
print_result("Create New Account role as button", new.get_attribute("role") == "button")
print_result("Create New Account button color as expected",
             new.value_of_css_property("background-color") == "rgba(66, 183, 42, 1)")

# Create a Page
create_page = driver.find_element(By.ID, "reg_pages_msg")
print_result("Create Page text as Expected", create_page.text == "Create a Page for a celebrity, brand or business.")

# Create Page link
page_link = driver.find_element(By.CLASS_NAME, "_8esh")
print_result("Create a Page has a link", page_link.tag_name == 'a')

# Page Footer
footer = driver.find_element(By.ID, "pageFooter")
print_result("Page has a footer", footer.tag_name == "div")

# Language
language_element = driver.find_element(By.CLASS_NAME, "localeSelectorList")
languages = language_element.text.split("\n")
print_result("Expected no of Languages available", len(languages) == 11)
print_result("English (UK) language present", "English (UK)" in languages)
print_result("हिन्दी language present", "हिन्दी" in languages)

# Footer Children link
children = driver.find_elements(By.XPATH, "//div[@id='pageFooterChildren']//ul//li")
print_result("Expected no of Child link present", len(children) == 31)

# Copyright in footer
copyright = driver.find_element(By.CLASS_NAME, "copyright")
print_result("Copyright available", copyright.is_displayed())
print_result("Copyright text as expected", copyright.text == "Meta © 2023")

# Testing Login Form with Data
email = driver.find_element(By.ID, "email")
pswd = driver.find_element(By.ID, "pass")
login_btn = driver.find_element(By.NAME, "login")

# Test Email Error
email.click()
pswd.click()
login_btn.click()
print_result("Redirected to new URL", driver.current_url != current_link)

login_error_img = driver.find_element(By.CLASS_NAME, "_9ay6").tag_name
print_result("Login Input Error image present", login_error_img == 'img')

login_error_msg = driver.find_element(By.CLASS_NAME, "_9ay7")
expected_login_error = "The email address or mobile number you entered isn't connected to an account. Find your account and log in."
print_result("Login Error Message as expected", login_error_msg == expected_login_error)

print_result("Error Message text color should be red", login_error_msg.value_of_css_property("color") == "rgba(240, 40, 73, 1)")
print_result("Find your account and log in text has a link", driver.find_element(By.XPATH, "//div[@class='_9ay7']//a").is_displayed())

# Password Error
driver.find_element(By.ID, "email").send_keys("salmankhan")
driver.find_element(By.ID, "pass").send_keys("")
driver.find_element(By.NAME, "login").click()
pass_error = driver.find_element(By.CLASS_NAME, "_9ay7").text
print_result("Password Error Message without password", pass_error == "The password that you've entered is incorrect. Forgotten password?")

# Password Error
driver.find_element(By.ID, "email").clear()
driver.find_element(By.ID, "email").send_keys("salmankhan")
driver.find_element(By.ID, "pass").send_keys("Salmankhan")
driver.find_element(By.NAME, "login").click()
pass_error = driver.find_element(By.CLASS_NAME, "_9ay7").text
print_result("Password Error Message with incorrect password", pass_error == "The password that you've entered is incorrect. Forgotten password?")

# Close the browser window
driver.quit()
