import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ulilities.Read_Config_File import ReadConfigFile

url = ReadConfigFile.get_sf_url()
username = ReadConfigFile.get_sf_username()
password = ReadConfigFile.get_sf_password()


@pytest.fixture()
def login_to_salesforce():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(url)
    driver.find_element_by_xpath("//input[@type='email']").send_keys(username)
    driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    driver.find_element_by_xpath("//input[@id='Login']").click()
    return driver