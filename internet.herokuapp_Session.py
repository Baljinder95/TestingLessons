import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains

driver = webdriver.Chrome(executable_path="D://chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(text(),'A/B Testing')]").click()
# source=driver.find_element(By.XPATH,"//a[contains(text(),'A/B Testing')]")
# action =ActionChains(driver)
# action.context_click(source).perform()

cap = driver.find_element(By.TAG_NAME,"h3").text
print(cap)
# assert "A/B Test Variation 1" == cap

Capture=driver.find_element(By.TAG_NAME,"p").text
print(Capture)
time.sleep(2)

#New Season For Test
driver.back()

time.sleep(2)

driver.find_element(By.XPATH,"//a[contains(text(),'Add/Remove Elements')]").click()
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(2)
