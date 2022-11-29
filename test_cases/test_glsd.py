from data import reading_objects
from POM.glassdoor import Search
import pytest

data_obj = reading_objects.read_test_data()
@pytest.mark.parametrize("data_",data_obj)

class TestFuncBar:

    def test_Search2(self,_driver,data_):
        sp = Search(_driver)
        sp.search(data_)
        sp.login_()
        sp.log_pwd(data_)
        sp.submit_()
        sp.TF_search(data_)
        sp.btn_()
        sp.L_item()
        sp.loc("Pune(India)")
        sp.loc1()



















