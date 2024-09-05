import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_demowebshop.POM.homepage import HomePage

# def test_check_for_login(driver):
#     home_page_obj = HomePage(driver)
#     home_page_obj.click_on_login()
#     allure.attach(driver.get_screenshot_as_png(),name="test_check_for_login.png",attachment_type=AttachmentType.PNG)
#
#
# def test_check_for_register(driver):
#     home_page_obj = HomePage(driver)
#     home_page_obj.click_on_register()


@pytest.mark.xfail
def test_sample():
    print("Expected pass")

def test_sample2():
    print("Expected pass sample2")
    assert True

@pytest.mark.xfail
def test_sample3():
    print("Expected fail")
    assert False