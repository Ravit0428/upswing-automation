import unittest
from selenium.webdriver.common.by   import By
from base_test import BaseTest

class TestSanity(BaseTest):

    def test_sanity(self):
        with self.subTest("Verify Login Button Available"):
            self.assertTrue(self.isElementPresent(By.ID, "login2"), "Login Button Not Found")
        with self.subTest("Verify Singup Button Available"):
            self.assertTrue(self.isElementPresent(By.ID, "signin2"), "Singup Button Not Found")

if __name__ == "__main__":
    unittest.main()
