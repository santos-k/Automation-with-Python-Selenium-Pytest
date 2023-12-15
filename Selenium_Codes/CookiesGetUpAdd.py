# Get and add cookies
from selenium import webdriver

# Create a webdriver instance (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://demo.nopcommerce.com/")

# Get All Cookies
cookies = driver.get_cookies()

type(cookies)

# First Cookie details
cookies[1]

for cookie in cookies:
    print(cookie,"\n")

# Get one cookie by cookie name
cookie1 = driver.get_cookie(".Nop.Culture")
print(cookie1)

print("Domain: ", cookie1.get("domain"))

for key in cookie1:
    print(f"{key.ljust(10)} : {cookie[key]}")

print("No of cookies present before: ", len(cookies))

# Add a new cookie
driver.add_cookie({"name":"credential","value":"username"})

updated_cookies = driver.get_cookies()
print("No of cookies present after add new cookie: ", len(updated_cookies))

for key in updated_cookies:
    print("Cookie name: ",key['name'])

driver.quit()
