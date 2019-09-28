from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        self.browser.implicitly_wait(3)
        super(NewVisitorTest, self).setUp()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_whether_satisfies_user_needs(self):
        # Arga Ghulam Ahmad just implemented a personal homepage. He goes to checkout him personal homepage.
        self.browser.get(self.live_server_url)

        # He notices the page title mention Arga Ghulam Ahmad's Homepage.
        home_page_title = 'Arga Ghulam Ahmad - Homepage - To-Do lists'

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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Arga has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He want to know what the system's feedback when there is no to-do
        todo_feedback = self.browser.find_element_by_id("todo-feedback")
        self.assertEqual("Yeahh, tidak ada tugas. Main game ahh.", todo_feedback.text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy peacock feathers" into a text box (Arga's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When He hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # He want to know what the system's feedback when there is a to-do
        todo_feedback = self.browser.find_element_by_id("todo-feedback")
        self.assertEqual("Kerjain ahhh, biar cepat kelar.", todo_feedback.text)

        # There is still a text box inviting HIm to add another item. He
        # enters "Use peacock feathers to make a fly" (Arga is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on HIm list
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # He is invited to enter some to-do items, to check what the system feedback after he input 5 to-do items in
        # total
        for i in range(3):
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Another todo' + str(i))
            inputbox.send_keys(Keys.ENTER)

        todo_feedback = self.browser.find_element_by_id("todo-feedback")
        self.assertEqual("Oh tidakk, kerjaan ku banyak.", todo_feedback.text)

        # Arga wonders whether the site will remember HIm list. Then He sees
        # that the site has generated a unique URL for HIm -- there is some
        # explanatory text to that effect.

        # He visits that URL - HIm to-do list is still there.

        # Satisfied, He goes back to sleep
