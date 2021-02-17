from selenium import webdriver
from POB import locator
from POB import signuppage
from POB import searchpage
from selenium.webdriver.common.by import By

class SelectPage:
    def __init__(self,driver):
        self.select_btn=driver.find_element(By.XPATH,locator.select_btn)
        self.continue_btn=driver.find_element(By.XPATH,locator.continue_btn)

    def getSelect_Btn(self):
        return self.select_btn

    def getContinue_Btn(self):
        return self.continue_btn