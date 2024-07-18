import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
from base_test import BaseTest

class TestSanity(BaseTest):

    def test_sanity(self):
        with self.subTest("Verify Login Button Available"):
            self.assertTrue(self.is_element_present(By.ID, "login2"), "Login Button Not Found")
        with self.subTest("Verify Singup Button Available"):
            self.assertTrue(self.is_element_present(By.ID, "signin2"), "Singup Button Not Found")

if __name__ == "__main__":
    unittest.main()
