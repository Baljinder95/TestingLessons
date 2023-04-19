import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(text(),'Dynamic Loading')]").click()
time.sleep(4)

Text1 = driver.find_element(By.TAG_NAME,"h3").text
print(Text1)
time.sleep(5)

driver.find_element(By.XPATH,"//a[contains(text(),'Example 2:')]").click()
time.sleep(8)







driver.find_element(By.XPATH,"//button[contains(text(),'Start')]").click()
time.sleep(10)


Text2 = driver.find_element(By.CSS_SELECTOR,"#finish").text
print(Text2)