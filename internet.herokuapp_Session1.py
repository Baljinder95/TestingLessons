import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains

driver = webdriver.Chrome(executable_path="D://chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(text(),'Add/Remove Elements')]").click()
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(10)
driver.find_element(By.XPATH,"//button[contains(text(),'Delete')]").click()
time.sleep(10)