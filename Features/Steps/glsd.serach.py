from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@given(u'Open the browser and enter valid URL and click on continue with email')
def step_impl(context):
    path = r"C:\Users\ASUS\OneDrive\Desktop\driverfiles\chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.get("https://www.glassdoor.co.in/member/home/index.htm")
    context.driver.maximize_window()
    # context.driver.implicitly_wait(50)
    time.sleep(2)
    context.driver.find_element("id", "inlineUserEmail").send_keys("devyanilute51@gmail.com")
    time.sleep(2)
    context.driver.find_element("name", "submit").click()
    time.sleep(2)


@given(u'Enter the password and click on signin')
def step_impl(context):
    context.driver.find_element("id", "inlineUserPassword").send_keys("Glassdoor@123")
    context.driver.find_element("name", "submit").click()
    time.sleep(2)

@then(u'Enter the text in search textfield')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@type='text']").send_keys("Software Engineer")
    time.sleep(2)


@then(u'Click on search button1')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Search']").click()


@then(u'Click on list search bar9')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@aria-label='Search Context Picker']").click()


@then(u'Select the job option')
def step_impl(context):
    context.driver.find_element("id","option_0").click()
    time.sleep(2)


@then(u'Click on search button2')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Search']").click()
    time.sleep(2)


@then(u'Navigate to back page01')
def step_impl(context):
    context.driver.back()


@then(u'Click on list search bar8')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@aria-label='Search Context Picker']").click()
    time.sleep(2)


@then(u'select the companies option')
def step_impl(context):
    context.driver.find_element("id","option_1").click()
    time.sleep(2)


@then(u'Click on search button3')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Search']").click()
    time.sleep(2)


@then(u'Navigate to back page02')
def step_impl(context):
    context.driver.back()


@then(u'Click on list search bar7')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@aria-label='Search Context Picker']").click()
    time.sleep(2)


@then(u'Select the salaries option')
def step_impl(context):
    context.driver.find_element("id","option_2").click()
    time.sleep(2)


@then(u'Click on search button4')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Search']").click()
    time.sleep(1)


@then(u'Navigate to back page03')
def step_impl(context):
    context.driver.back()


@then(u'Click on list search bar6')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@aria-label='Search Context Picker']").click()
    time.sleep(2)

@then(u'Select the interviews option')
def step_impl(context):
    context.driver.find_element("id","option_3").click()
    time.sleep(2)


@then(u'Click on search button5')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Search']").click()


@then(u'Navigate to back page04')
def step_impl(context):
    context.driver.back()


@then(u'Click on Location bar')
def step_impl(context):
    context.a_obj = ActionChains(context.driver)
    obj_ = context.driver.find_element("xpath", "//input[@placeholder='Location']")
    context.a_obj.double_click(obj_).perform()
    context.a_obj.key_down(Keys.CONTROL).send_keys("X").key_up(Keys.CONTROL).perform()
    time.sleep(4)


@then(u'Enter the location')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@id='sc.location']").send_keys("Pune(India)")
    time.sleep(2)


@then(u'Click on search button6')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Search']").click()
    time.sleep(2)

@then(u'Close the browser')
def step_impl(context):
    context.driver.close()
