import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUser()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("*** Started Login Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUser(self.user)
        self.lp.setPass(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title=="Swag Labs":
            self.logger.info("*** test passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** test failed ***")
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            assert False





