import unittest
from selenium.webdriver.common.by   import By
from base_test import BaseTest

class TestSignup(BaseTest):

    def test_singup(self):
        with self.subTest("Click on Signup"):
            self.clickOnInput(By.ID,"signin2")
        with self.subTest("Enter Username"):
            self.enterInput(By.ID,"sign-username", self.generateRandomUsername())
        with self.subTest("Enter Password"):
            self.enterInput(By.ID,"sign-password","test")
        with self.subTest("Signup"):
            self.clickOnInput(By.XPATH,"//*[@id='signInModal']/div/div/div[3]/button[2]")
        with self.subTest("Verify Successful Singup"):
            self.assertTrue(self.isAlertPresent("Sign up successful."), "Alert did not appear")

class TestSignupWithBlankInputs(BaseTest):

    def test_singup_with_blank(self):
        with self.subTest("Click on Signup"):
            self.clickOnInput(By.ID,"signin2")
        with self.subTest("Signup"):
            self.clickOnInput(By.XPATH,"//*[@id='signInModal']/div/div/div[3]/button[2]")
        with self.subTest("Verify Successful Singup"):
            self.assertTrue(self.isAlertPresent("Please fill out Username and Password."), "Alert did not appear")

class TestSignupWithExistingUser(BaseTest):

    def test_singup_with_existing_user(self):
        with self.subTest("Click on Signup"):
            self.clickOnInput(By.ID,"signin2")
        with self.subTest("Enter Existing Username"):
            self.enterInput(By.ID,"sign-username", "test")
        with self.subTest("Enter Password"):
            self.enterInput(By.ID,"sign-password","test")
        with self.subTest("Signup"):
            self.clickOnInput(By.XPATH,"//*[@id='signInModal']/div/div/div[3]/button[2]")
        with self.subTest("Verify Successful Singup"):
            self.assertTrue(self.isAlertPresent("This user already exist."), "Alert did not appear")

if __name__ == "__main__":
    unittest.main()
