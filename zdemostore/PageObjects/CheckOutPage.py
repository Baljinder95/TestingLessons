from driver import driver
from selenium.webdriver.common.by import By

class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver


    cart = (By.XPATH,"//ul[@id='site-header-cart']")

    def Cartitem(self):

        return self.driver.find_element(*CheckOutPage.cart)


    ship = (By.ID,"shipping_method_0_flat_rate1")

    def Shipitem(self):
        return self.driver.find_element(*CheckOutPage.ship)


    Proced = (By.XPATH,"//a[contains(text(),'Proceed to checkout')]")


    def Process(self):
        return  self.driver.find_element(*CheckOutPage.Proced)

    First = (By.NAME,"billing_first_name")

    def name(self):
        return self.driver.find_element(*CheckOutPage.First)

    Last= (By.NAME,"billing_last_name")

    def Lname(self):
        return self.driver.find_element(*CheckOutPage.Last)

    Company=(By.ID,"billing_company")

    def company(self):
        return self.driver.find_element(*CheckOutPage.Company)


    # driver.find_element(By.XPATH, "//ul[@id='site-header-cart']").click()
    # time.sleep(1)
    # driver.find_element(By.ID, "shipping_method_0_flat_rate1").click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").click()
    # time.sleep(1)
    #
    # driver.find_element(By.NAME, "billing_first_name").send_keys("Baljinder")
    # driver.find_element(By.NAME, "billing_last_name").send_keys("Singh")
    # driver.find_element(By.ID, "billing_company").send_keys("Testing")
    # driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
    # time.sleep(5)