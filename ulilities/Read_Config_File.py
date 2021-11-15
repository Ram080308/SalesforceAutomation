import configparser
config = configparser.RawConfigParser()
config.read("E:\\Salesforce_TestAutomation\\test_data\\config.ini")

class ReadConfigFile:
    @staticmethod
    def get_sf_url():
        sf_url = config.get("SF Login","url")
        return sf_url

    @staticmethod
    def get_sf_username():
        sf_username = config.get("SF Login","username")
        return sf_username

    @staticmethod
    def get_sf_password():
        sf_password = config.get("SF Login","password")
        return sf_password


