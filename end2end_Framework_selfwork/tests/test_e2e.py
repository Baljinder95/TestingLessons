import time
from typing import Self

import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from end2end_Framework_selfwork.pageObjects.Checkoutpage import Checkoutpage
from end2end_Framework_selfwork.pageObjects.ConfirmPage import ConfirmPage
from end2end_Framework_selfwork.pageObjects.LoginPage import LoginPage
from end2end_Framework_selfwork.utilities.BaseClass import BaseClass



class TestOne(BaseClass):

    def test_e2e(self,setup):


        logg=LoginPage(self.driver)
        logg.user().send_keys("standard_user")
        logg.pas().send_keys("secret_sauce")
        logg.log().click()
        time.sleep(10)

        Check = Checkoutpage(self.driver)
        Check.add1().click()
        Check.add2().click()
        Check.add3().click()
        Check.add4().click()
        Check.cartt().click()
        Check.shopp().click()
        Check.out().click()


        confim = ConfirmPage(self.driver)

        confim.Ist().send_keys("Baljinder")
        confim.IInd().send_keys("Singh")
        confim.zip().send_keys("L6Y 5E3")
        time.sleep(10)
        confim.placing().click()
        confim.finaly().click()
