from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Arga Ghulam Ahmad - Homepage - To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

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
