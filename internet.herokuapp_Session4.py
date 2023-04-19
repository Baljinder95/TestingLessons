import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(text(),'Dynamic Controls')]").click()
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Remove')]").click()
time.sleep(5)
Text = driver.find_element(By.ID,"message").text
print(Text)
assert driver.find_element(By.ID,"message").text =="It's gone!"
time.sleep(4)

driver.find_element(By.XPATH,"//button[contains(text(),'Enable')]").click()
time.sleep(8)

driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("Baljinder")
Text2 = driver.find_element(By.XPATH,"//p[@id='message']").text
print(Text2)
time.sleep(10)