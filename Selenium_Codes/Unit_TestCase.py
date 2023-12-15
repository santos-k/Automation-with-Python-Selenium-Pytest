import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

opt = Options()
opt.add_experimental_option('detach', True)


class GoogleSearch(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        print("Page Title: ", self.driver.title)

    def test_Search(self):
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        self.element = self.driver.find_element(By.NAME, "q")
        self.element.send_keys("Unittest Python")
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        self.element2 = self.driver.find_element(By.XPATH, "//div[@class='yuRUbf']//a")
        self.element2.click()
        print("Page Title: ", self.driver.title)


if __name__ == "__main__":
    unittest.main()
