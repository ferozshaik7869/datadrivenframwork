from selenium import webdriver
from selenium.webdriver.common.by import By
from POB import locator
from POB import signuppage


# class LoginPage:
#     def __init__(self,driver):
#         self.txt_username=driver.find_element(By.ID,locator.username_id)
#         self.txt_password=driver.find_element(By.ID,locator.password_id)
#         self.btn_login=driver.find_element(By.XPATH,locator.btn_login_xpath)
#         self.btn_create_new=driver.find_element(By.XPATH,locator.btn_create_newxpath)
#
#     def getTxtUserName(self):
#         return self.txt_username
#     def getTxtPassWord(self):
#         return self.txt_password
#     def getBtnLogin(self):
#         return self.btn_login
#     def getBtnCreateNew(self):
#         return self.btn_create_new
# ******************************************
# #adactine hotel page login
from selenium import webdriver
from POB import locator
from POB import signuppage
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.txt_username=driver.find_element(By.XPATH,locator.usernameid)
        self.txt_password=driver.find_element(By.XPATH,locator.passwordid)
        self.btn_login=driver.find_element(By.XPATH,locator.login_btn)
    def getTUserName(self):
        return self.txt_username

    def getTPassWord(self):
        return self.txt_password

    def getBTNLogin(self):
        return self.btn_login

# from selenium import webdriver
# from POB import locator
# from POB import signuppage
# from POB import searchpage
# from selenium.webdriver.common.by import By
#
# class SelectPage:
#         def __init__(self, driver):
#             self.select_btn = driver.find_element(By.XPATH, locator.select_btn)
#             self.continue_btn = driver.find_element(By.XPATH, locator.continue_btn)
#
#         def getSelect_Btn(self):
#             return self.select_btn
#
#         def getContinue_Btn(self):
#             return self.continue_btn
# from selenium.webdriver.common.by import By
# from POB import locator
# from POB import loginpage
# from POB import signuppage
# from POB import selectpage
# from POB import searchpage
#
# class LogoutPage:
#     def __init__(self,driver):
#         self.logout_btn=driver.find_element(By.XPATH,locator.logout_btn)
#     def getLogOut(self):
#         return self.logout_btn
# from selenium import webdriver
# from POB import locator
# from POB import signuppage
# from POB import searchpage
# from selenium.webdriver.common.by import By
#
# class SearchPage:
#     def __init__(self,driver):
#         self.loction=driver.find_element(By.XPATH,locator.location)
#         self.hotels=driver.find_element(By.XPATH,locator.hotels)
#         self.room_types=driver.find_element(By.XPATH,locator.room_type)
#         self.room_no=driver.find_element(By.XPATH,locator.room_no)
#         self.check_indate=driver.find_element(By.XPATH,locator.check_indate)
#         self.check_outdate=driver.find_element(By.XPATH,locator.check_outdate)
#         self.adult_room=driver.find_element(By.XPATH,locator.adult_room)
#         self.child_room=driver.find_element(By.XPATH,locator.child_room)
#         self.search_btn=driver.find_element(By.XPATH,locator.search_btn)
#
#     def getLoction(self):
#         return self.loction
#
#     def getHotel(self):
#         return self.hotels
#
#     def getRoomType(self):
#         return self.room_types
#
#     def getRoomNo(self):
#         return self.room_no
#
#     def getCheckInDate(self):
#         return self.check_indate
#
#     def getCheckOutDate(self):
#         return self.check_outdate
#
#     def getAdultRoom(self):
#         return self.adult_room
#
#     def getChildRoom(self):
#         return self.child_room
#
#     def getSearch_Btn(self):
#         return self.search_btn