from selenium import webdriver
from selenium.webdriver.common.by import By
from POB.loginpage import LoginPage
from POB.loginpage import LoginPage
# from test.employee import *
# class login(Base):
#     def login_functionality(self):
#         b=Base()
#         d= b.launch_browser()
#         n= b.load_url("https://www.facebook.com/")
#         print(n,type(n))
#         l=LoginPage(d)
#         b.type(l.getTxtUserName(),"mohammadferoz_210@yagoo.co.in")
#         b.type(l.getTxtPassWord(),"shareef@yasin")
        #refresh
        # b.refresh()
        # l2=SignUp(d)
        # b.type(l2.getFirstName(),"Feroz")
        # b.type(l2.getSurName(),"shaik")

#
# l1=login()
# l1.login_functionality()
# *******************************************
# from globalclass.calssBase import Base
# from POB import locator
# class login(Base):
#     def login_functionality(self):
#         driver=self.launch_browser()
#         self.load_url("https://www.facebook.com/")
#         lr=LoginPage(driver)
#         self.type(lr.getTxtUserName().self.get_data_from_excel(r"C:\Users\Admin\Desktop\feroz.xlsx)",2,1))
#         self.type(lr.getTxtPassWord().self.get_data_from_excel(r"C:\Users\Admin\Desktop\feroz.xlsx",2,2))
#         self.btn_login(lr.getBtnLogin())
# lk=login()
# lk.login_functionality()





from selenium import webdriver
from selenium.webdriver.common.by import By
from globalclass.calssBase import Base
from POB.selectpage import SelectPage
from POB.searchpage import SearchPage
from POB.loginpage import LoginPage
from POB.logoutpage import LogoutPage
from POB.bookingpage import BookingPage


class Adactinehotel(Base):
    def booking(self):
        driver=self.launch_browser()
        self.load_url("https://adactinhotelapp.com/")
        ln=LoginPage(driver)
        self.type(ln.getTUserName(),"nitishselvakumar")
        self.type(ln.getTPassWord(),"s1740034")

        self.btn_click(ln.getBTNLogin())
        lm=SearchPage(driver)
        self.select_by_value(lm.getLoction(),"Paris")
        self.select_by_value(lm.getHotel(),"Hotel Sunshine")
        self.select_by_index(lm.getRoomType(),"3")
        self.select_by_index(lm.getRoomNo(),"4")
        self.type(lm.getCheckInDate(),"05/05/2020")
        self.type(lm.getCheckOutDate(),"20/05/2020")
        self.select_by_index(lm.getAdultRoom(),"2")
        self.select_by_index(lm.child_room,"4")
        self.btn_click(lm.getSearch_Btn())
        lo=SelectPage(driver)
        self.btn_click(lo.getSelect_Btn())
        self.btn_click(lo.getContinue_Btn())
        lj=BookingPage(driver)
        self.type(lj.getFirstName(),"feroz")
        self.type(lj.getLastName(),"shaik")
        self.type(lj.getBilling_Adress(),"chuttugunta,Guntur=Ap,India")
        self.type(lj.getCredit_cardNO(),"5411366544112436")
        self.select_by_value(lj.getCredit_cardType(),"VISA")

        self.select_by_index(lj.getEXpiry_Month(),"12")


        self.select_by_value(lj.getExpiry_Year(),"2022")


        self.type(lj.getCvv_No(),"7869")


        self.btn_click(lj.getBook_HotelRoom())


        li=LogoutPage(driver)

        # logout_btn=driver.find_element(By.XPATH,"//a[text()='Logout']")
        self.btn_click(li.getLogOut())

        self.quit_browser()

l2=Adactinehotel()
l2.booking()
#
#
