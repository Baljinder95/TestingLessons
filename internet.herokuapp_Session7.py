import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="D:\\chrome.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'WYSIWYG Editor')]").click()
time.sleep(10)

iframe=driver.find_element(By.CSS_SELECTOR,"body.mce-content-body:nth-child(2) > p:nth-child(1)").click()
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR,"body.mce-content-body:nth-child(2) > p:nth-child(1)").clear()
time.sleep(10)