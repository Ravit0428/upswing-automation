import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
from base_test import BaseTest
from selenium.common.exceptions import NoAlertPresentException

class TestLogin(BaseTest):

    def test_login(self):
        with self.subTest("Click on Login"):
            self.clickOnInput(By.ID,"login2")
        with self.subTest("Enter Username"):
            self.enterInput(By.ID,"loginusername","test")
        with self.subTest("Enter Password"):
            self.enterInput(By.ID,"loginpassword","test")
        with self.subTest("Log in"):
            self.clickOnInput(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")
        with self.subTest("Verify logged in"):
            self.assertTrue(self.is_element_present(By.ID, "nameofuser"), "Login Failed")

class TestInvalidLogin(BaseTest):

    def test_invalid_login(self):
        with self.subTest("Click on Login"):
            self.clickOnInput(By.ID,"login2")
        with self.subTest("Enter Username"):
            self.enterInput(By.ID,"loginusername","test")
        with self.subTest("Enter Password"):
            self.enterInput(By.ID,"loginpassword","password")
        with self.subTest("Log in"):
            self.clickOnInput(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")
        with self.subTest("Verify invalid alert"):
            self.assertTrue(self.is_alert_present(), "Alert did not appear")

    def is_alert_present(self):
        try:
            self.sleep()
            self.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

if __name__ == "__main__":
    unittest.main()
