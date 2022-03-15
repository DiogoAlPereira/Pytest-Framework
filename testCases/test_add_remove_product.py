import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.Products import Products
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_add_remove_product:
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUser()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_add_remove_product(self, setup):
        self.logger.info("*** Started Add and Remove Product Test ***")
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
        self.prod.clickRemoveBackpack()
        self.prod.clickMenu()
        self.prod.clickLogout()
        if act_title == "Swag Labs":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_logout.png")
            self.driver.close()
            assert False






