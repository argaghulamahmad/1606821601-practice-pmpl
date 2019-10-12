from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from .prod_base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # Arga has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get(self.server_url)

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

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

        # There is still a text box inviting Him to add another item. He
        # enters "Use peacock feathers to make a fly" (Arga is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on Him list
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Satisfied, He goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Arga starts a new to-do list
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # He notices that Him list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # He want to know what the system's feedback when there is a to-do
        todo_feedback = self.browser.find_element_by_id("todo-feedback")
        self.assertEqual("Kerjain ahhh, biar cepat kelar.", todo_feedback.text)

        # He is invited to enter some to-do items, to check what the system feedback after he input 5 to-do items in
        # total
        for i in range(4):
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Another todo' + str(i))
            inputbox.send_keys(Keys.ENTER)

        todo_feedback = self.browser.find_element_by_id("todo-feedback")
        self.assertEqual("Oh tidakk, kerjaan ku banyak.", todo_feedback.text)

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Arga's is coming through from cookies etc
        self.browser.quit()
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        self.browser.implicitly_wait(3)

        # Francis visits the home page.  There is no sign of Arga's
        # list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Arga...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Arga's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep
