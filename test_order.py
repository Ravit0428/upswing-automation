import unittest
from selenium.webdriver.common.by   import By
from base_test import BaseTest

class OrderTest(BaseTest):
    
    def test_Order(self):
        with self.subTest("Click on Phones"):
            self.clickOnInput(By.LINK_TEXT,"Phones")
        with self.subTest(" Add to Samsung Product and click"):
            self.clickOnInput(By.LINK_TEXT,"Samsung galaxy s6")
        with self.subTest("Click on Add to cart Button"):
            self.clickOnInput(By.LINK_TEXT,"Add to cart")
        with self.subTest("verify Add to Cart Alert"):
            self.assertTrue(self.isAlertPresent("Product added"), "Alert did not appear")
            self.AcceptAlert()
        with self.subTest("Click on Cart"):
            self.clickOnInput(By.LINK_TEXT,"Cart")
        with self.subTest("Click on Place Order"):
            self.clickOnInput(By.XPATH,"//*[@id='page-wrapper']/div/div[2]/button")
        with self.subTest("Field The Name "):
            self.enterInput(By.ID,"name","Ravi")
        with self.subTest("Field The Country "):
            self.enterInput(By.ID,"country","India")
        with self.subTest("Field The City "):
            self.enterInput(By.ID,"city","Pune")
        with self.subTest("Field The Credit card"):
            self.enterInput(By.ID,"card","HDFC")
        with self.subTest("Field The Month"):
            self.enterInput(By.ID,"month","June")
        with self.subTest("Field The Year"):
            self.enterInput(By.ID,"year","2024")
        with self.subTest("Click On Purchase"):
            self.clickOnInput(By.XPATH,"//*[@id='orderModal']/div/div/div[3]/button[2]")

class TestPlaceOrderBlankInputs(BaseTest):

    def test_PlaceOrder_blank(self):
        with self.subTest("Click on Cart"):
            self.clickOnInput(By.LINK_TEXT,"Cart")
        with self.subTest("Click on Place Order"):
            self.clickOnInput(By.XPATH,"//*[@id='page-wrapper']/div/div[2]/button")
        with self.subTest("Field The Name "):
            self.enterInput(By.ID,"name","Ravi")
        with self.subTest("Field The Country "):
            self.enterInput(By.ID,"country","India")
        with self.subTest("Field The City "):
            self.enterInput(By.ID,"city","Pune")
        with self.subTest("Field The Credit card"):
            self.enterInput(By.ID,"card","HDFC")
        with self.subTest("Field The Month"):
            self.enterInput(By.ID,"month","June")
        with self.subTest("Field The Year"):
            self.enterInput(By.ID,"year","2024")
        with self.subTest("Click On Purchase"):
            self.clickOnInput(By.XPATH,"//*[@id='orderModal']/div/div/div[3]/button[2]")






if __name__ == "__main__":
    unittest.main()
           