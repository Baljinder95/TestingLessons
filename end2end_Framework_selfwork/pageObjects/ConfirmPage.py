import time

import driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    first = (By.NAME, "firstName")
    last = (By.ID, "last-name")
    zipcode = (By.XPATH, "//input[@placeholder='Zip/Postal Code']")
    Cont=(By.ID,"continue")
    final=(By.NAME,"finish")
    def Ist(self):
        return self.driver.find_element(*ConfirmPage.first)

    def IInd(self):
        return self.driver.find_element(*ConfirmPage.last)

    def zip(self):
        return self.driver.find_element(*ConfirmPage.zipcode)

    def placing(self):
        return self.driver.find_element(*ConfirmPage.Cont)

    def finaly(self):
        return self.driver.find_element(*ConfirmPage.final)

    # driver.find_element(By.ID, "continue").click()
    # driver.find_element(By.NAME, "finish").click()