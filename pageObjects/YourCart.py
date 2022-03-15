import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class YourCart:
    btnMenu_id = "react-burger-menu-btn"
    lnkLogout_id = "logout_sidebar_link"
    btnRemoveBackpack_id = "remove-sauce-labs-backpack"
    btnCart_id = "shopping_cart_container"
    btnCheckout_id = "checkout"


    def __init__(self, driver):
        self.driver = driver

    def clickMenu(self):
        self.driver.find_element(By.ID, self.btnMenu_id).click()

    def clickLogout(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, self.lnkLogout_id))).click()
        except TimeoutException:
            return False
        return True

    def clickRemoveBackpack(self):
        self.driver.find_element(By.ID, self.btnRemoveBackpack_id).click()

    def clickCart(self):
        self.driver.find_element(By.ID, self.btnCart_id).click()

    def clickCheckout(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, self.btnCheckout_id))).click()
        except TimeoutException:
            return False
        return True
