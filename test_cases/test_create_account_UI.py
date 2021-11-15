from ulilities.Read_Config_File import ReadConfigFile
from page_objects.SF_Home_Page import SF_HomePage
from page_objects.SF_Accounts_Home_Page import SF_AccountsHomePage
from page_objects.SF_New_Account_Creation_page import SF_AccountCreationPage

class Test_CreateAccountFromSF_UI:
    url = ReadConfigFile.get_sf_url()
    username = ReadConfigFile.get_sf_username()
    password = ReadConfigFile.get_sf_password()

    def test_create_account_from_UI(self,login_to_salesforce):
        self.driver = login_to_salesforce

        self.sf_homepage = SF_HomePage(self.driver)
        self.sf_homepage.test_click_accounts_link()

        self.sf_accounts_home_page = SF_AccountsHomePage(self.driver)
        self.sf_accounts_home_page.test_click_new_button()

        self.sf_new_acc_create_page = SF_AccountCreationPage(self.driver)
        self.sf_new_acc_create_page.test_create_new_account("TestPythonAccount","Security User")
