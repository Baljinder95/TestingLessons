import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chrome.exe")
driver.get("https://www.saucedemo.com/?ref=hackernoon.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("performance_glitch_user")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR,"#login-button").click()
driver.find_element(By.XPATH,"(//button[@class='btn btn_primary btn_small btn_inventory'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//button[@class='btn btn_primary btn_small btn_inventory'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//button[@class='btn btn_primary btn_small btn_inventory'])[3]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
time.sleep(2)
driver.find_element(By.ID,"shopping_cart_container").click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#checkout").click()
driver.find_element(By.NAME,"firstName").send_keys("Baljinder")
driver.find_element(By.ID,"last-name").send_keys("Singh")
driver.find_element(By.XPATH,"//input[@placeholder='Zip/Postal Code']").send_keys("L6Y 5E3")
driver.find_element(By.ID,"continue").click()
driver.find_element(By.NAME,"finish").click()
Cap=driver.find_element(By.TAG_NAME,"h2").text
print(Cap)
Cap2 = driver.find_element(By.XPATH,"//div[contains(text(),'Your order has been dispatched')]").text
print(Cap2)
assert Cap2 == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"


time.sleep(4)