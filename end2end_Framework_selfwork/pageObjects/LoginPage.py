import time

import driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    username = (By.NAME, "user-name")
    password = (By.NAME, "password")
    login = (By.ID, "login-button")

    def user(self):
        return self.driver.find_element(*LoginPage.username)

    def pas(self):
        return self.driver.find_element(*LoginPage.password)

    def log(self):
        return self.driver.find_element(*LoginPage.login)
