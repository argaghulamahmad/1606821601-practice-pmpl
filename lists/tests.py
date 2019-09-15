from django.test import TestCase


class SmokeTests(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
