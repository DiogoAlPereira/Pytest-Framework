import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_login_error:
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUser()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login_error(self, setup):
        self.logger.info("*** Started Login Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUser("test")
        self.lp.setPass(self.password)
        self.lp.clickLogin()
        self.lp.getError()
        self.driver.close()






