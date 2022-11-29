import pytest
from selenium import webdriver
from library_.config import Config
import time
# from selenium.webdriver.firefox.options import Options

@pytest.fixture(params=["Chrome","Edge"])
def _driver(request):
    if request.param == "Chrome":
        driver_1 = webdriver.Chrome(executable_path=Config.Chrome_Driver_path)

    # elif request.param == "Firefox":
    #     options = Options()
    #     options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    #     driver_1 = webdriver.Firefox(executable_path=Config.Firefox_Driver_path,options=options)

    elif request.param == "Edge":
        driver_1 = webdriver.Edge(executable_path=Config.Edge_Driver_path)

    driver_1.get(Config.URL)
    driver_1.maximize_window()
    driver_1.implicitly_wait(30)
    yield driver_1
    print(driver_1.title)
    time.sleep(2)
    driver_1.save_screenshot("test_glass.png")
    driver_1.close()