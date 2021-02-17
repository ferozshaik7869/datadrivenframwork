from selenium import webdriver
from POB import locator
from POB import signuppage
from POB import searchpage
from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self,driver):
        self.loction=driver.find_element(By.XPATH,locator.location)
        self.hotels=driver.find_element(By.XPATH,locator.hotels)
        self.room_types=driver.find_element(By.XPATH,locator.room_type)
        self.room_no=driver.find_element(By.XPATH,locator.room_no)
        self.check_indate=driver.find_element(By.XPATH,locator.check_indate)
        self.check_outdate=driver.find_element(By.XPATH,locator.check_outdate)
        self.adult_room=driver.find_element(By.XPATH,locator.adult_room)
        self.child_room=driver.find_element(By.XPATH,locator.child_room)
        self.search_btn=driver.find_element(By.XPATH,locator.search_btn)

    def getLoction(self):
        return self.loction

    def getHotel(self):
        return self.hotels

    def getRoomType(self):
        return self.room_types

    def getRoomNo(self):
        return self.room_no

    def getCheckInDate(self):
        return self.check_indate

    def getCheckOutDate(self):
        return self.check_outdate

    def getAdultRoom(self):
        return self.adult_room

    def getChildRoom(self):
        return self.child_room

    def getSearch_Btn(self):
        return self.search_btn