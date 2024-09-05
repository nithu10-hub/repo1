from pytest_demowebshop.POM.homepage import HomePage
from pytest_demowebshop.POM.register import Register



# def test_register_with_all_valid_input(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register()
#     register.register_an_account("nithya","dharshini","nithya10@gmail.com","123456","123456")
#     assert driver.find_element("xpath", "//input[@value='nithya10@gmail.com']").is_displayed()

# def test_register_with_out_fname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register()
#     register.register_an_account("","dharshini","nithya10@gmail.com","123456","123456")
#     assert driver.find_element("xpath", "//input[@value='nithya10@gmail.com']").is_displayed()
#
#
# def test_register_with_out_lname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register()
#     register.register_an_account("nithya","","nithya10@gmail.com","123456","123456")
#     assert driver.find_element("xpath", "//input[@value='nithya10@gmail.com']").is_displayed()
#
#
# def test_register_with_out_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register()
#     register.register_an_account("nithya","dharshini","","123456","123456")
#     assert driver.find_element("xpath", "//input[@value='nithya10@gmail.com']").is_displayed()

#
# def test_register_with_out_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register()
#     register.register_an_account("nithya","dharshini","nithya10@gmail.com","","123456")
#     assert driver.find_element("xpath", "//input[@value='nithya10@gmail.com']").is_displayed()
#
#
# def test_register_with_out_cpassword(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register()
#     register.register_an_account("nithya","dharshini","nithya10@gmail.com","123456","")
#     assert driver.find_element("xpath", "//input[@value='nithya10@gmail.com']").is_displayed()
#
#
# def test_register_with_out_any_input(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register()
#     register.register_an_account("","","","","")
#     assert driver.find_element("xpath", "//input[@value='nithya10@gmail.com']").is_displayed()

