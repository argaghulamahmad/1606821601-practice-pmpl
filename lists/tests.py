from django.test import TestCase
from django.urls import resolve

from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Arga Ghulam Ahmad - Homepage - To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'homepage.html')

    def test_whether_home_page_title_same_as_intended(self):
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        home_page_title = '<title>Arga Ghulam Ahmad - Homepage - To-Do lists</title>'
        self.assertIn(home_page_title, html_response)

    def test_the_owner_informations_appears_at_home_page(self):
        response = self.client.get('/')
        html_response = response.content.decode('utf8')

        owner_name = "Arga Ghulam Ahmad"
        owner_id = "1606821601"
        owner_major = "Ilmu Komputer"

        self.assertIn(owner_name, html_response)
        self.assertIn(owner_id, html_response)
        self.assertIn(owner_major, html_response)

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_todo_feedback_when_numbers_of_todo_equal_zero(self):
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        self.assertIn('Yeahh, tidak ada tugas. Main game ahh.', html_response)

    def test_todo_feedback_when_numbers_of_todo_less_than_five_case1(self):
        for i in range(1):
            self.client.post('/', data={'item_text': 'A new list item'})
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        self.assertIn('Kerjain ahhh, biar cepat kelar.', html_response)

    def test_todo_feedback_when_numbers_of_todo_less_than_five_case2(self):
        for i in range(2):
            self.client.post('/', data={'item_text': 'A new list item'})
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        self.assertIn('Kerjain ahhh, biar cepat kelar.', html_response)

    def test_todo_feedback_when_numbers_of_todo_less_than_five_case3(self):
        for i in range(3):
            self.client.post('/', data={'item_text': 'A new list item'})
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        self.assertIn('Kerjain ahhh, biar cepat kelar.', html_response)

    def test_todo_feedback_when_numbers_of_todo_less_than_five_case4(self):
        for i in range(4):
            self.client.post('/', data={'item_text': 'A new list item'})
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        self.assertIn('Kerjain ahhh, biar cepat kelar.', html_response)

    def test_todo_feedback_when_numbers_of_todo_equal_five(self):
        for i in range(5):
            self.client.post('/', data={'item_text': 'A new list item'})
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        self.assertIn('Oh tidakk, kerjaan ku banyak.', html_response)

    def test_todo_feedback_when_numbers_of_todo_more_than_five(self):
        for i in range(6):
            self.client.post('/', data={'item_text': 'A new list item'})
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        self.assertIn('Oh tidakk, kerjaan ku banyak.', html_response)

    def test_todo_feedback_when_numbers_of_todo_equal_one_hundred(self):
        for i in range(100):
            self.client.post('/', data={'item_text': 'A new list item'})
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        self.assertIn('Oh tidakk, kerjaan ku banyak.', html_response)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
