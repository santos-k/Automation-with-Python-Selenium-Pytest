# Get Table content
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

testauto = "https://testautomationpractice.blogspot.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(testauto)

# no of rows
table_row = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print("No of Rows in Table including heading: ", len(table_row))

# No of columns
table_col = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
print("No of Columns in Table: ", len(table_col))

# table data
for row in range(2, len(table_row)+1):
    for col in range(1, len(table_col)+1):
        data = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{row}]//td[{col}]").text
        print(data.ljust(20), end=" ")
    print("")

# table data based on conditions(list of books whose author is Mukesh)
books_ls = []
for row in range(2, len(table_row)+1):
    author = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{row}]//td[2]").text
    if author == "Mukesh":
        books = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{row}]//td[1]").text
        books_ls.append(books)
print("Books Written by Mukesh: ", books_ls)


# table data based on conditions(list of books those price is => 1000)
books_ls = []
for row in range(2, len(table_row)+1):
    price = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{row}]//td[4]").text
    if int(price) >= 1000:
        books = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{row}]//td[1]").text
        books_ls.append(books)
print("Books Price greater then 1000: ", books_ls)

time.sleep(5)
driver.quit()
