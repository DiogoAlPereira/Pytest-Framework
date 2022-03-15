import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Login:
    txtUser_id = "user-name"
    txtPassword_id = "password"
    btnLogin_id = "login-button"
    txtError_tag = "h3"

    def __init__(self, driver):
        self.driver = driver

    def setUser(self, user):
        self.driver.find_element(By.ID, self.txtUser_id).clear()
        self.driver.find_element(By.ID, self.txtUser_id).send_keys(user)

    def setPass(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).clear()
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.btnLogin_id).click()

    def getError(self):
        self.driver.find_element(By.TAG_NAME, self.txtError_tag)
        assert "Epic sadface: Username and password do not match any user in this service" in self.driver.page_source