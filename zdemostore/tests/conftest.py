import time
import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait





def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome"

    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name =request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver= webdriver.Chrome(executable_path="D://chromedriver.exe")
    elif browser_name == "Firefox":
        driver = webdriver.Firefox(executable_path="D://geckodriver.exe")

    print(driver.title)
    driver.maximize_window()
    driver.get("http://demostore.supersqa.com/")
    request.cls.driver =driver
    yield
    driver.close()