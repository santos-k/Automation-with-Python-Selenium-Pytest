from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)


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


driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Login
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.current_url)
print(driver.title)

# Find Logo
logo = check_element_displayed(By.XPATH,"//div[@class='oxd-brand-banner']//img")
print_result("Logo Available",logo)

# Header Text
header = check_element_text(By.XPATH, "//div[@class='oxd-topbar-header-title']//h6", "Dashboard")
print_result("Header Title", header)

# User Profile Icon
profile_photo = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-img").is_displayed()
print_result("User Profile Photo Displayed", profile_photo)

# User Name
profile_name = check_element_text(By.CLASS_NAME,"oxd-userdropdown-name", "Paul Collings")
print_result("User Name displayed as expected", profile_name)

# Click dropdown and find lists
driver.find_element(By.CLASS_NAME, "oxd-userdropdown-icon").click()

profile_menu = driver.find_elements(By.CLASS_NAME, "oxd-userdropdown-link")
print_result("Options in Profile menu as expected", (len(profile_menu) == 4))

side_menu = driver.find_elements(By.CLASS_NAME, "oxd-main-menu-item-wrapper")
side_menu_lists = []
for menu in side_menu:
    side_menu_lists.append(menu.text)
print_result("No of side menu option lists expected", len(side_menu)==12)
