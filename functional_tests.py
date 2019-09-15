from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_whether_satisfies_user_needs(self):
        # These comments are User Story that describes how the app will work from the point of view of the user. Used
        # to structure a functional test.

        # Arga Ghulam Ahmad just implemented a personal homepage. He goes to checkout him personal homepage.
        self.browser.get('http://localhost:8000')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
