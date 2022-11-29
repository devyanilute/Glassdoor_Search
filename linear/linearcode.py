from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
path = r"C:\Users\ASUS\OneDrive\Desktop\driverfiles\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(50)

driver.get("https://www.glassdoor.co.in/member/home/index.htm")
driver.maximize_window()
time.sleep(2)

#Login'''

driver.find_element("id","inlineUserEmail").send_keys("devyanilute51@gmail.com")
time.sleep(2)
driver.find_element("name","submit").click()
time.sleep(2)
driver.find_element("id","inlineUserPassword").send_keys("Glassdoor@123")
driver.find_element("name","submit").click()


#Search Textfield'''

# TC_search_valid_data_software engineer
driver.find_element("xpath","//input[@type='text']").send_keys("Software Engineer")
driver.find_element("xpath","//span[text()='Search']").click()
# driver.find_element("name","jobTitle").send_keys("software Engineer")
# time.sleep(2)
# driver.find_element("xpath","//button[@class='gd-ui-button editState e8e8plt0 css-1kp7eb7']").click()
# time.sleep(2)
# driver.find_element("xpath","//span[@class='SVGInline modal_closeIcon']").click()
# driver.close()

#list search bar'''

list_ = ["Jobs", "Companies", "Salaries", "Interviews"]
for item in list_:
    tre = driver.find_element("xpath", "(//div[@class='selectedLabel'])[1]")
    tre.click()
    driver.find_element("xpath",f"//span[text()='{item}']").click()
    time.sleep(2)
    driver.find_element("xpath","//span[text()='Search']").click()
    # time.sleep(3)
    if item == ["Salaries","Interviews"]:
        pass
    else:
        driver.back()

#placeholder search bar'''
# change bangalore to pune

a_obj = ActionChains(driver)
obj_ = driver.find_element("xpath", "//input[@placeholder='Location']")
a_obj.double_click(obj_).perform()
a_obj.key_down(Keys.CONTROL).send_keys("X").key_up(Keys.CONTROL).perform()
driver.find_element("xpath", "//input[@id='sc.location']").send_keys("Pune(India)")
driver.find_element("xpath", "//button[@type='submit']").click()

driver.close()

# driver.find_element("name", "jobTitle").send_keys("Bank manager")
# driver.find_element("xpath", "//button[@class='gd-ui-button editState e8e8plt0 css-1kp7eb7']").click()
# driver.find_element("xpath", "//span[@class='SVGInline modal_closeIcon']").click()
















        # driver.find_element("xpath", "//span[text()='Add Review or Salary']").click()
        # driver.find_element("xpath", "//div[text()='Salary']").click()
        # driver.find_element("xpath", "//input[@name='survey-inputFields-component']").send_keys("Manual Tester")
        # driver.find_element("xpath", "//div[@class='styles__footer__copyright d-flex flex-column align-items-center px-lg pt-std pb-std my-0 mx-auto']").click()
        # driver.find_element("name", "jobTitle").send_keys("Project manager")
        # driver.find_element("xpath", "//button[@class='gd-ui-button editState e8e8plt0 css-1kp7eb7']").click()
        # driver.find_element("xpath", "//span[@class='SVGInline modal_closeIcon']").click()
        # driver.find_element("xpath", "//span[text()='Next']").click()
        # driver.find_element("id", "basePay").send_keys("4,00,000")
    # else item == 'Interviews':
    #     pass





# job = driver.find_elements("xpath","//li[@role='option']")
# for item in job[1]:
#     job[item].click()
#     driver.find_element("xpath","//button[@type='submit']").click()
#     continue
# time.sleep(30)

# jobs
# driver.find_element("xpath","(//div[@class='selectedLabel'])[1]").click()
# driver.find_element("id","option_0").click()
# driver.find_element("xpath","//button[@type='submit']").click()
# time.sleep(2)
# driver.find_element("name","jobTitle").send_keys("software Engineer")
# time.sleep(2)
# driver.find_element("xpath","//button[@class='gd-ui-button editState e8e8plt0 css-1kp7eb7']").click()
# driver.find_element("xpath","//span[@class='SVGInline modal_closeIcon']").click()
# driver.back()
# time.sleep(4)

# Companies
# driver.find_element("xpath","(//div[@class='selectedLabel'])[1]").click()
# driver.find_element("id","option_1").click()
# driver.find_element("xpath","//button[@type='submit']").click()
# time.sleep(2)
# driver.find_element("name","jobTitle").send_keys("software Engineer")
# time.sleep(2)
# driver.find_element("xpath","//button[@class='gd-ui-button editState e8e8plt0 css-1kp7eb7']").click()
# driver.find_element("xpath","//span[@class='SVGInline modal_closeIcon']").click()
# time.sleep(4)

# salaries
# driver.find_element("xpath","//div[@class='selectedLabel']").click()
# driver.find_element("id","option_2").click()
# driver.find_element("xpath","//button[@type='submit']").click()
#
# driver.find_element("xpath","//span[text()='Add Review or Salary']").click()
# driver.find_element("xpath","//div[text()='Salary']").click()
# driver.find_element("xpath","//input[@name='survey-inputFields-component']").send_keys("Automation Tester")
#
# driver.find_element("name","jobTitle").send_keys("Project manager")
# driver.find_element("xpath","//button[@class='gd-ui-button editState e8e8plt0 css-1kp7eb7']").click()
# driver.find_element("xpath","//span[@class='SVGInline modal_closeIcon']").click()

# interviews
# driver.find_element("xpath","//div[@class='selectedLabel']").click()
# driver.find_element("id","option_3").click()
# driver.find_element("xpath","//button[@type='submit']").click()
#
# driver.find_element("name","jobTitle").send_keys("Analyst")
# driver.find_element("xpath","//button[@class='gd-ui-button editState e8e8plt0 css-1kp7eb7']").click()
# driver.find_element("xpath","//span[@class='SVGInline modal_closeIcon']").click()


