import unittest
from selenium.webdriver.common.by   import By
from base_test import BaseTest

class ProductBrowsing(BaseTest):

    def test_Categories(self):
        with self.subTest("Click on Phones"):
            self.clickOnInput(By.LINK_TEXT,"Phones")
        with self.subTest("Verify Samsung is present"):
           self.assertTrue(self.isElementPresent(By.LINK_TEXT,"Samsung galaxy s6"))
        with self.subTest("Click on Laptops"):
            self.clickOnInput(By.LINK_TEXT,"Laptops")
        with self.subTest("Verify Sony vaio i5 is present"):
           self.assertTrue(self.isElementPresent(By.LINK_TEXT,"Sony vaio i5"))
        with self.subTest("Click on Monitors"):
            self.clickOnInput(By.LINK_TEXT,"Monitors")
        with self.subTest("Verify Apple monitor 24 is present"):
           self.assertTrue(self.isElementPresent(By.LINK_TEXT,"Apple monitor 24"))
    
class ProductNevigated(BaseTest):

    def test_Nevigated(self):
        with self.subTest("Click on Nextbutton"):
            self.clickOnInput(By.ID,"next2")
        with self.subTest("verify Mackbook is present"):
            self.assertTrue(self.isElementPresent(By.LINK_TEXT,"MacBook air"))
        with self.subTest("Click on Previous"):
            self.clickOnInput(By.ID,"prev2")

            
        



if __name__ == "__main__":
    unittest.main()