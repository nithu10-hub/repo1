from pytest_demowebshop.POM.homepage import HomePage

class Register(HomePage):
    gender = ("id","gender-female")
    first_name = ("id","FirstName")
    last_name = ("id","LastName")
    email = ("id","Email")
    password = ("id","Password")
    confirm_password = ("id","ConfirmPassword")
    submit = ("id","register-button")

    def register_an_account(self,fname,lname,email,password,cpassword):

        self.click_on_an_element(self.gender)
        self.send_text_to_an_element(self.first_name,fname)
        self.send_text_to_an_element(self.last_name,lname)
        self.send_text_to_an_element(self.email,email)
        self.send_text_to_an_element(self.password,password)
        self.send_text_to_an_element(self.confirm_password,cpassword)
        self.click_on_an_element(self.submit)
