from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('homepage.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_whether_home_page_title_same_as_intended(self):
        response = self.client.get('/')
        html_response = response.content.decode('utf8')
        home_page_title = '<title>Arga Ghulam Ahmad - Homepage</title>'
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
