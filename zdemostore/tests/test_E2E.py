import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from end2end_Framework_selfwork.utilities.BaseClass import BaseClass
from zdemostore.PageObjects.CheckOutPage import CheckOutPage
from zdemostore.PageObjects.HomePage import HomePage



class TestOne(BaseClass):

    def test_e2e(self, setup):

        homepage = HomePage(self.driver)
        homepage.shopitem1().click()
        homepage.shopitem2().click()
        homepage.shopitem3().click()


        check = CheckOutPage(self.driver)
        check.Cartitem().click()
        check.Shipitem().click()
        check.Process().click()
        check.name().send_keys("Baljinder")
        check.Lname().send_keys("Singh")
        check.company().send_keys("Testing")

        time.sleep(10)
        self.driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
        time.sleep(5)

        country = self.driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys("Can")
        results = self.driver.find_elements(By.XPATH, "(//ul[@class='select2-results__options'])[1]/li")
        print(len(results))
        for result in results:
            if "Canada" in result.text:
                result.click()
                time.sleep(4)
                break
        time.sleep(10)
        self.driver.find_element(By.ID, "billing_address_1").send_keys("15 Lanyard")
        self.driver.find_element(By.ID, "billing_city").send_keys("North York")
        self.driver.find_element(By.XPATH, "//span[@id='select2-billing_state-container']").click()
        time.sleep(10)

        self.driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys("Ont")
        time.sleep(5)
        states = self.driver.find_elements(By.XPATH, "(//ul[@class='select2-results__options'])[1]/li")
        print(len(states))
        for state in states:
            if "Ontario" in state.text:
                state.click()
                time.sleep(4)
                break
        time.sleep(10)

        self.driver.find_element(By.NAME, "billing_postcode").send_keys("L6Y5E3")
        self.driver.find_element(By.ID, "billing_phone").send_keys("1234567890")

        self.driver.find_element(By.NAME, "billing_email").send_keys("King@gmail.com")

        self.driver.find_element(By.XPATH, "//button[@class='button alt']").click()

        time.sleep(10)




