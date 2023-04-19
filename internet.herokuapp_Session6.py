import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="D:\\chrome.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'Floating Menu')]").click()
time.sleep(10)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(10)