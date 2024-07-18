import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by   import By

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/")
        with self.subTest("Verify Store is accessible"):
            self.assertIn("STORE", self.driver.title)
    
    def sleep(self):
        time.sleep(1)

    def enterInput(self, by, search, input):
        self.sleep()
        self.driver.find_element(by, search).send_keys(input)
    
    def clickOnInput(self, by, search):
        self.sleep()
        self.driver.find_element(by, search).click()

    def is_element_present(self, how, what):
        self.sleep()
        try:
            self.driver.find_element(how, what)
        except:
            return False
        return True
    
    def tearDown(self):
        self.driver.quit()