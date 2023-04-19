from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self,driver):
        self.driver = driver


    item1 =(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[1]")


    def shopitem1(self):
        return self.driver.find_element(*HomePage.item1)

    item2 = (By.XPATH, "(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[1]")

    def shopitem2(self):
        return self.driver.find_element(*HomePage.item2)


    item3 = (By.XPATH, "(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[1]")

    def shopitem3(self):
        return self.driver.find_element(*HomePage.item3)



#
#
# driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[1]").click()
# time.sleep(1)
# driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[2]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[3]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[4]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[6]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[7]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[8]").click()
