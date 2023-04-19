import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D://chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'Dynamic Content')]").click()

Text1 = driver.find_element(By.TAG_NAME,"h3").text
print(Text1)

Text2 = driver.find_element(By.XPATH,"//p[contains(text(),'This example')]").text
print(Text2)

driver.find_element(By.XPATH,"//a[contains(text(),'click here')]").click()


Text3 = driver.find_element(By.XPATH,"//div[contains(text(),'Omnis fugiat ')]").text
print(Text3)
time.sleep(4)