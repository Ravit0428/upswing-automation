import unittest
from selenium.webdriver.common.by   import By
from base_test import BaseTest

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
            self.assertTrue(self.isElementPresent(By.ID, "nameofuser"), "Login Failed")

class TestWrongPasswordLogin(BaseTest):

    def test_wrong_password_login(self):
        with self.subTest("Click on Login"):
            self.clickOnInput(By.ID,"login2")
        with self.subTest("Enter Username"):
            self.enterInput(By.ID,"loginusername","test")
        with self.subTest("Enter Password"):
            self.enterInput(By.ID,"loginpassword","password")
        with self.subTest("Log in"):
            self.clickOnInput(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")
        with self.subTest("Verify invalid alert"):
            self.assertTrue(self.isAlertPresent("Wrong password."), "Alert did not appear")

class TestWrongUserLogin(BaseTest):

    def test_wrong_user_login(self):
        with self.subTest("Click on Login"):
            self.clickOnInput(By.ID,"login2")
        with self.subTest("Enter Username"):
            self.enterInput(By.ID,"loginusername","sdfsdsa")
        with self.subTest("Enter Password"):
            self.enterInput(By.ID,"loginpassword","password")
        with self.subTest("Log in"):
            self.clickOnInput(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")
        with self.subTest("Verify invalid alert"):
            self.assertTrue(self.isAlertPresent("User does not exist."), "Alert did not appear")

if __name__ == "__main__":
    unittest.main()
