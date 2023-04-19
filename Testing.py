from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Click Here").click()
wind= driver.window_handles

driver.switch_to.window(wind[1])
print (driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(wind[0])
assert "Opening a new window" ==driver.find_element(By.TAG_NAME,"h3").text

