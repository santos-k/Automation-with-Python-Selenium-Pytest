# Delete cookies
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

# Get All Cookies
cookies = driver.get_cookies()
print("Total No of Cookies", len(cookies))
for i in cookies:
    print(i, "\n")


# delete a cookie by name
cookie_name = '.Nop.Customer'
driver.delete_cookie(cookie_name)
print(f"Cookie {cookie_name} deleted")

print("Updated  Cookies: ", len(driver.get_cookies()))

driver.delete_all_cookies()
print("Delete all cookies")

print("Updated  Cookies: ", len(driver.get_cookies()))

driver.quit()
