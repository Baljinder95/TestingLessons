import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="D://chromedriver.exe")
driver.get("http://demostore.supersqa.com/")
driver.set_window_size(1001, 1001)
time.sleep(1)

driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[3]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[4]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[6]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[7]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[8]").click()
time.sleep(1)



driver.find_element(By.XPATH, "//ul[@id='site-header-cart']").click()
time.sleep(1)
driver.find_element(By.ID, "shipping_method_0_flat_rate1").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").click()
time.sleep(1)

driver.find_element(By.NAME, "billing_first_name").send_keys("Baljinder")
driver.find_element(By.NAME, "billing_last_name").send_keys("Singh")
driver.find_element(By.ID, "billing_company").send_keys("Testing")
driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
time.sleep(5)


country = driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys("Can")
results = driver.find_elements(By.XPATH,"(//ul[@class='select2-results__options'])[1]/li")
print(len(results))
for result in results:
    if "Canada" in result.text:
        result.click()
        time.sleep(4)
        break
time.sleep(10)
driver.find_element(By.ID,"billing_address_1").send_keys("15 Lanyard")
driver.find_element(By.ID,"billing_city").send_keys("North York")
driver.find_element(By.XPATH,"//span[@id='select2-billing_state-container']").click()
time.sleep(10)

driver.find_element(By.XPATH,"//input[@class='select2-search__field']").send_keys("Ont")
time.sleep(5)
states = driver.find_elements(By.XPATH ,"(//ul[@class='select2-results__options'])[1]/li")
print(len(states))
for state in states:
    if "Ontario" in state.text:
        state.click()
        time.sleep(4)
        break
time.sleep(10)


driver.find_element(By.NAME,"billing_postcode").send_keys("L6Y5E3")
driver.find_element(By.ID,"billing_phone").send_keys("1234567890")

driver.find_element(By.NAME,"billing_email").send_keys("King@gmail.com")

driver.find_element(By.XPATH,"//button[@class='button alt']").click()

time.sleep(10)
