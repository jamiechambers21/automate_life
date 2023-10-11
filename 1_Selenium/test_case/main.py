import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):


    # Always run in order
    # setUp >> test >> tearDown, setUp >> test >> tearDown
    def setUp(self):
        print("setup")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://www.python.org/")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()