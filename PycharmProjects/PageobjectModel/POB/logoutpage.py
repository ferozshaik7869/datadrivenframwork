from selenium.webdriver.common.by import By
from POB import locator
from POB import loginpage
from POB import signuppage
from POB import selectpage
from POB import searchpage

class LogoutPage:
    def __init__(self,driver):
        self.logout_btn=driver.find_element(By.XPATH,locator.logout_btn)
    def getLogOut(self):
        return self.logout_btn