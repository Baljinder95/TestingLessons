import time

import driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    Item1 = (By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory'])[1]")
    Item2 = (By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory'])[2]")
    Item3 = (By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory'])[3]")
    Item4 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    Cart = (By.ID, "shopping_cart_container")
    shop = (By.XPATH, "//a[@class='shopping_cart_link']")
    checkout1 = (By.CSS_SELECTOR, "#checkout")

    #driver.find_element(By.NAME, "firstName").send_keys("Baljinder")

    def add1(self):
        return self.driver.find_element(*Checkoutpage.Item1)

    def add2(self):
        return self.driver.find_element(*Checkoutpage.Item2)

    def add3(self):
        return self.driver.find_element(*Checkoutpage.Item3)

    def add4(self):
        return self.driver.find_element(*Checkoutpage.Item4)

    def cartt(self):
        return self.driver.find_element(*Checkoutpage.Cart)

    def shopp(self):
        return self.driver.find_element(*Checkoutpage.shop)

    def out(self):
        return self.driver.find_element(*Checkoutpage.checkout1)

#
#
#
# driver.find_element(By.XPATH,"(//button[@class='btn btn_primary btn_small btn_inventory'])[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//button[@class='btn btn_primary btn_small btn_inventory'])[2]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//button[@class='btn btn_primary btn_small btn_inventory'])[3]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
# time.sleep(2)
# driver.find_element(By.ID,"shopping_cart_container").click()
# driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"#checkout").click()


# driver.find_element(By.NAME,"firstName").send_keys("Baljinder")
# driver.find_element(By.ID,"last-name").send_keys("Singh")
# driver.find_element(By.XPATH,"//input[@placeholder='Zip/Postal Code']").send_keys("L6Y 5E3")
# driver.find_element(By.ID,"continue").click()
# driver.find_element(By.NAME,"finish").click()
# Cap=driver.find_element(By.TAG_NAME,"h2").text