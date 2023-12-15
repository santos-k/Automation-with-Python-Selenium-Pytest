from selenium import webdriver
import time

# Provide authentication credentials
username = "admin"
password = "admin"

# Create a WebDriver instance
driver = webdriver.Chrome()

# Construct the URL with authentication credentials
url_with_credentials = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

# Navigate to the URL
driver.get(url_with_credentials)
print("Page Title: ",driver.title)
print("Page URL: ", driver.current_url)

# Continue interacting with the page as needed

time.sleep(3)
# Close the browser window
driver.quit()
