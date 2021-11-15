from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SF_AccountCreationPage:
    accountname_field_xpath = "//input[@name='acc2']"
    acc_type_dropdown_xpath = "//select[@name='acc6']"
    acc_industry_dropdown_xpath = "//select[@name='acc7']"
    acc_manager_lookup_xpath = "//img[@title='Account Manager Lookup (New Window)']"
    seacrh_field_xpath = "//input[@id='lksrch']"
    go_button_xpath = "//input[@type='submit']"
    searchresults_link_xpath = "//a[text()='Security User']"
    save_button_xpath = "//input[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def test_create_new_account(self, acc_name,acc_manager):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.acc_manager_lookup_xpath)))
        self.driver.find_element_by_xpath(self.accountname_field_xpath).send_keys(acc_name)
        acctype = Select(self.driver.find_element_by_xpath(self.acc_type_dropdown_xpath))
        acctype.select_by_visible_text("Customer - Direct")
        accind = Select(self.driver.find_element_by_xpath(self.acc_industry_dropdown_xpath))
        accind.select_by_visible_text("Apparel")
        self.driver.find_element_by_xpath(self.acc_manager_lookup_xpath).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.switch_to.frame("searchFrame")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.seacrh_field_xpath)))
        self.driver.find_element_by_xpath(self.seacrh_field_xpath).send_keys(acc_manager)
        self.driver.find_element_by_xpath(self.go_button_xpath).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("resultsFrame")
        wait.until(EC.element_to_be_clickable((By.XPATH, self.searchresults_link_xpath)))
        self.driver.find_element_by_xpath(self.go_button_xpath).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath(self.save_button_xpath).click()




