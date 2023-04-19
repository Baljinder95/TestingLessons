from selenium import  webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'Dropdown')]").click()
Cap=driver.find_element(By.TAG_NAME,"h3").text
print(Cap)
driver.find_element(By.ID,"dropdown").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"option[value='1']").click()
time.sleep(4)
