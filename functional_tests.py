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

        # He notices the page title mention Arga Ghulam Ahmad's Homepage.
        home_page_title = 'Arga Ghulam Ahmad - Homepage'

        self.assertIn(home_page_title, self.browser.title)

        # He want to check whether the information that displayed on the homepage is correct.
        owner_full_name = "Arga Ghulam Ahmad"
        owner_college_major = "Ilmu Komputer"
        owner_student_id = "1606821601"

        owner_full_name_element = self.browser.find_element_by_id("owner-full-name")
        owner_college_major_element = self.browser.find_element_by_id("owner-college-major")
        owner_student_id_element = self.browser.find_element_by_id("owner-student-id")

        self.assertEqual(owner_full_name, owner_full_name_element.text)
        self.assertEqual(owner_college_major, owner_college_major_element.text)
        self.assertEqual(owner_student_id, owner_student_id_element.text)

        # He satisfied and deploy the app to the server.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
