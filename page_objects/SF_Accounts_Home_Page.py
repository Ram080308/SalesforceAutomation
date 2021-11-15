from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SF_AccountsHomePage:
    new_button_xpath = "//input[@value=' New ']"

    def __init__(self,driver):
        self.driver = driver

    def test_click_new_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.new_button_xpath)))
        self.driver.find_element_by_xpath(self.new_button_xpath).click()