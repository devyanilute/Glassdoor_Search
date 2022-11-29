import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from library_.config import Config
from data import reading_objects

search_obj = reading_objects.read_locators()

class Search:
    def __init__(self,driver_1):
        self.driver_1 = driver_1

#Login
    def search(self,data_):
        self.driver_1.find_element(*search_obj['Login-email']).send_keys(data_[0])
        time.sleep(2)

    def login_(self):
        self.driver_1.find_element(*search_obj['Login_button']).click()
        time.sleep(2)

    def log_pwd(self,data_):
        self.driver_1.find_element(*search_obj['login_pwd']).send_keys(data_[1])
        time.sleep(2)

    def submit_(self):
        self.driver_1.find_element(*search_obj['submit_button']).click()
        time.sleep(1)
        print("login is succesfull")

#Search TEXT FIELD

    def TF_search(self,data_):
        self.driver_1.find_element(*search_obj['search_TF']).send_keys(data_[2])
        time.sleep(4)

    def btn_(self):
        self.driver_1.find_element(*search_obj['search_btn']).click()
        time.sleep(6)

#List Search

    def L_item(self):
        list_ = ["Jobs","Companies","Salaries", "Interviews"]
        for item in list_:
            tre = self.driver_1.find_element("xpath", "(//div[@class='selectedLabel'])[1]")
            tre.click()
            time.sleep(4)
            self.driver_1.find_element("xpath", f"//span[text()='{item}']").click()
            time.sleep(5)
            self.driver_1.find_element("xpath", "//span[text()='Search']").click()
            time.sleep(3)
            if item == ["Salaries", "Interviews"]:
                pass
            else:
                self.driver_1.back()

#placeholder search bar
    def loc(self, location):
        self.location = location
        loc = self.driver_1.find_element(*search_obj['PH_bar_TF'])
        loc_obj = ActionChains(self.driver_1)
        loc_obj.double_click(loc).perform()
        loc_obj.send_keys_to_element(loc, f'{location}').perform()
        time.sleep(3)

    def loc1(self):
        loc1 = self.driver_1.find_element(*search_obj['search_button5']).click()
        time.sleep(2)

        # self.driver_1.close()


















    # def loc2(self):
    #     try:
    #         loc2 = self.driver_1.find_element(*search_obj['alert_popup5']).send_keys("Bank manager")
    #         loc3 = self.driver_1.find_element(*search_obj['Activate_button5']).click()
    #         loc4 = self.driver_1.find_element(*search_obj['Cross_key5']).click()
    #         time.sleep(2)
    #     except:
    #         pass


















            # self.driver_1.find_element(*search_obj['Job_Tf']).click()
            # time.sleep(2)
            # self.driver_1.find_element("xpath","//span[text()='Jobs']").click()
            # time.sleep(2)
            # self.driver_1.find_element(*search_obj['search_b']).click()
            # if item ==["Companies"]:
            #     self.driver_1.find_element("xpath","//span[text()='Companies']").click()
            #     self.driver_1.find_element("xpath","//span[text()='Search']").click()
            # else:
            #     self.driver_1.back()

    # def sea5(self):
    #     self.driver_1.find_element(*search_obj['job_0']).click()
    #     time.sleep(4)
    #
    # def sear(self):
    #     self.driver_1.find_element(*search_obj['Job_id']).click()
    #     time.sleep(4)
    #
    # def sear1(self):
    #     self.driver_1.find_element(*search_obj['Search_button1']).click()
    #     time.sleep(3)
#--------------------
    # def sear2(self):
    #     self.driver_1.find_element(*search_obj['job_alert1']).send_keys("software Engineer")
    #     time.sleep(3)
    #
    # def sear3(self):
    #     self.driver_1.find_element(*search_obj['Activate_button1']).click()
    #     time.sleep(3)
    #
    # def sear4(self):
    #     self.driver_1.find_element(*search_obj['Cross_key1']).click()
    #     time.sleep(2)

    # def sear5(self):
    #     self.driver_1.find_element(*search_obj['companies_TF']).click()
    #     time.sleep(2)
    #
    # def sear6(self):
    #     self.driver_1.find_element(*search_obj['companies_id']).click()
    #     time.sleep(2)
    #
    # def sear7(self):
    #     self.driver_1.find_element(*search_obj['search_button2']).click()
    #     time.sleep(2)

    # def sear8(self):
    #     self.driver_1.find_element(*search_obj['job_alert2']).send_keys("software Engineer")
    #     time.sleep(2)

    # def star(self):
    #     self.driver_1.find_element(*search_obj['Activate_button2']).click()
    #     time.sleep(2)
    #
    # def star1(self):
    #     self.driver_1.find_element(*search_obj['Cross_key2']).click()
    #     time.sleep(2)
    #
    # def star2(self):
    #     self.driver_1.find_element(*search_obj['salaries_TF']).click()
    #     time.sleep(2)
    #
    # def star3(self):
    #     self.driver_1.find_element(*search_obj['salaries_id']).click()
    #     time.sleep(2)
    #
    # def star4(self):
    #     self.driver_1.find_element(*search_obj['Search_button3']).click()
    #     time.sleep(4)

    # def star05(self):
    #     self.driver_1.find_element(*search_obj['add_review']).click()
    #     time.sleep(2)
    #
    # def star06(self):
    #     self.driver_1.find_element(*search_obj['radio_btnsal']).click()
    #     time.sleep(2)

    # def star5(self):
    #     self.driver_1.find_element(*search_obj['salary_alert3']).send_keys("Project manager")
    #     time.sleep(2)
    #
    # def star6(self):
    #     self.driver_1.find_element(*search_obj['Activate_button3']).click()
    #     time.sleep(2)

    # def star7(self):
    #     self.driver_1.find_element(*search_obj['Cross_key3']).click()
    #     time.sleep(2)
    #
    # def star8(self):
    #     self.driver_1.find_element(*search_obj['interview_TF']).click()
    #     time.sleep(2)
    #
    # def star9(self):
    #     self.driver_1.find_element(*search_obj['interview_id']).click()
    #     time.sleep(2)
    #
    # def star01(self):
    #     self.driver_1.find_element(*search_obj['search_button4']).click()
    #     time.sleep(2)

    # def star02(self):
    #     self.driver_1.find_element(*search_obj['alert_popup4']).send_keys("Analyst")
    #     time.sleep(2)
    #
    # def star03(self):
    #     self.driver_1.find_element(*search_obj['Activate_button4']).click()
    #     time.sleep(2)
    #
    # def star04(self):
    #     self.driver_1.find_element(*search_obj['Cross_key4']).click()
    #     time.sleep(2)

    # def star05(self):
    #     self.driver_1.find_element(*search_obj['PH_bar_TF']).click()
    #     time.sleep(2)
    #
    # def star06(self):
    #     self.driver_1.find_element(*search_obj['id_loc']).send_keys("Pune(India)")
    #     time.sleep(2)
    #
    # def star07(self):
    #     self.driver_1.find_element(*search_obj['search_button5']).click()
    #     time.sleep(2)
    #
    # def star08(self):
    #     self.driver_1.find_element(*search_obj['alert_popup5']).send_keys("Bank manager")
    #     time.sleep(2)
    #
    # def star09(self):
    #     self.driver_1.find_element(*search_obj['Activate_button5']).click()
    #     time.sleep(2)
    #
    # def star00(self):
    #     self.driver_1.find_element(*search_obj['Cross_key5']).click()
    #     time.sleep(2)




    # def loc3(self):
    #     loc3 = self.driver_1.find_element(*search_obj['Activate_button5']).click()
    #     time.sleep(2)
    #
    # def loc4(self):
    #     loc4 = self.driver_1.find_element(*search_obj['Cross_key5']).click()
    #     time.sleep(2)
