import pytest
from pytest_demowebshop.POM.homepage import HomePage
from pytest_demowebshop.POM.loginpage import LogIn


# username = [("reddyvinuth27@gmail.com","selenium"),("abc@gmail.com","adc"),("mno@gmail.com","mno"),("xyz@gmail.com","xyz")]
#
# @pytest.mark.parametrize("username,password",username)
# def test_login_with_proper_credentials(driver,username,password):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application(username,password)
#     assert driver.find_element("xpath", f"//a[.='{username}']").is_displayed()
#
# @pytest.mark.skip
# def test_login_with_no_password(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("reddyvinuth27@gmail.com", "")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()
#
# @pytest.mark.skip
# def test_login_with_no_username(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("", "selenium")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()
#
# @pytest.mark.skip
# def test_login_with_no_credentials(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("", "")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()
#
# @pytest.mark.skip
# def test_login_with_invalid_credentials(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("abc@gmail.com", "wastejava")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()



