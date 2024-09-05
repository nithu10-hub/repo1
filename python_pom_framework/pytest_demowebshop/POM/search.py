from pytest_demowebshop.POM.homepage import HomePage

class Search(HomePage):
    search_tab = ("id","small-searchterms")
    search_icon = ("xpath","//input[@type='submit']")

    def search_an_element(self,search):
        self.send_text_to_an_element(self.search_tab,search)
        self.click_on_an_element(self.search_icon)
