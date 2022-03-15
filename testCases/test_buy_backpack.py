import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.Products import Products
from pageObjects.YourCart import YourCart
from pageObjects.Checkout import Checkout
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_buy_backpack:
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUser()
    password = ReadConfig.getPassword()
    firstname = ReadConfig.getFirstName()
    lastname = ReadConfig.getLastName()
    zipcode = ReadConfig.getZipCode()

    logger = LogGen.loggen()

    def test_buy_backpack(self, setup):
        self.logger.info("*** Started Buy BackpackTest ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUser(self.user)
        self.lp.setPass(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title=="Swag Labs":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            assert False
        self.prod = Products(self.driver)
        self.prod.clickAddBackpack()
        self.prod.clickCart()
        self.cart = YourCart(self.driver)
        self.cart.clickCheckout()
        self.check = Checkout(self.driver)
        self.check.setFirstName(self.firstname)
        self.check.setLastName(self.lastname)
        self.check.setZipCode(self.zipcode)
        self.check.clickContinue()
        self.check.getTitle()
        self.check.clickFinish()
        self.check.getConfirmationText()
        self.prod.clickMenu()
        self.prod.clickLogout()
        if act_title == "Swag Labs":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_logout.png")
            self.driver.close()
            assert False






