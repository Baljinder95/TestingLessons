
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="D://chromedriver.exe")

driver.set_window_size(1000,1000)
time.sleep(5)


driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# identify dropdown with Select class
sel = Select(driver.find_element_by_xpath("//select[@name='continents']"))
#select by select_by_visible_text() method
sel.select_by_visible_text("Europe")
time.sleep(0.8)
#select by select_by_index() method
sel.select_by_index(0)
driver.close()