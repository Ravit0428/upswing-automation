import unittest
import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.by   import By
from selenium.common.exceptions import NoAlertPresentException

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/")
        with self.subTest("Verify Store is accessible"):
            self.assertIn("STORE", self.driver.title)
    
    def sleep(self):
        time.sleep(5)

    def enterInput(self, by, search, input):
        self.sleep()
        self.driver.find_element(by, search).send_keys(input)
    
    def clickOnInput(self, by, search):
        self.sleep()
        self.driver.find_element(by, search).click()

    def isElementPresent(self, how, what):
        self.sleep()
        try:
            self.driver.find_element(how, what)
        except:
            return False
        return True  

    def generateRandomUsername(self):
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for _ in range(10))
        return random_string

    def isAlertPresent(self, message):
        try:
            self.sleep()
            return self.driver.switch_to.alert.text == message
        except NoAlertPresentException:
            return False
    
    def tearDown(self):
        self.driver.quit()

    def AcceptAlert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        