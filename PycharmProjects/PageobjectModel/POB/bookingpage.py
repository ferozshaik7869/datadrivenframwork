from selenium  import webdriver
from POB import locator
from POB import searchpage
from POB import signuppage
from POB import selectpage
from selenium.webdriver.common.by import By

class BookingPage:
    def __init__(self,driver):
        self.first_name=driver.find_element(By.XPATH,locator.first_name)
        self.last_name=driver.find_element(By.XPATH,locator.last_name)
        self.billing_adress=driver.find_element(By.XPATH,locator.billing_address)
        self.credit_cardno=driver.find_element(By.XPATH,locator.credit_CardNo)
        self.credit_cardtype=driver.find_element(By.XPATH,locator.credit_cardType)
        self.Expiry_month=driver.find_element(By.XPATH,locator.Expiry_month)
        self.Expiry_year=driver.find_element(By.XPATH,locator.Expiry_year)
        self.Cvv_no=driver.find_element(By.XPATH,locator.Cvv_No)
        self.Book_hotelroom=driver.find_element(By.XPATH,locator.Book_hotelroom)

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getBilling_Adress(self):
        return self.billing_adress

    def getCredit_cardNO(self):
        return self.credit_cardno

    def getCredit_cardType(self):
        return self.credit_cardtype

    def getEXpiry_Month(self):
        return self.Expiry_month

    def getExpiry_Year(self):
        return self.Expiry_year

    def getCvv_No(self):
        return self.Cvv_no

    def getBook_HotelRoom(self):
        return self.Book_hotelroom