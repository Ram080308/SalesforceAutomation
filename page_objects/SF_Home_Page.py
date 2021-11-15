from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SF_HomePage:
    accounts_link_xpath = "//a[text()='Accounts']"

    def __init__(self,driver):
        self.driver = driver

    def test_click_accounts_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.accounts_link_xpath)))
        self.driver.find_element_by_xpath(self.accounts_link_xpath).click()




