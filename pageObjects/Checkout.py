import time
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Checkout:
    btnMenu_id = "react-burger-menu-btn"
    lnkLogout_id = "logout_sidebar_link"
    btnRemoveBackpack_id = "remove-sauce-labs-backpack"
    btnCart_id = "shopping_cart_container"
    btnCheckout_id = "checkout"
    txtFirstName_id = "first-name"
    txtLastName_id = "last-name"
    txtZipCode_id = "postal-code"
    btnContinue_id = "continue"
    txtTitle_class = "title"
    btnFinish_id = "finish"
    txtConfirmationText_class = "complete-text"


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
        self.driver.find_element(By.ID, self.btnCheckout_id).click()

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastname)

    def setZipCode(self, zipcode):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtZipCode_id).send_keys(zipcode)

    def clickContinue(self):
        self.driver.find_element(By.ID, self.btnContinue_id).click()

    def getTitle(self):
        title = self.driver.find_element(By.CLASS_NAME, self.txtTitle_class)
        assert title.text == "CHECKOUT: OVERVIEW"

    def clickFinish(self):
        self.driver.find_element(By.ID, self.btnFinish_id).click()

    def getConfirmationText(self):
        self.driver.find_element(By.CLASS_NAME, self.txtConfirmationText_class)
        assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in self.driver.page_source

