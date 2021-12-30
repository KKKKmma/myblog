from django.urls import reverse, resolve
from django.test import TestCase
from mainsite.views import homepage

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        # reverse：反查URL
        # resolve：解析
        found = resolve('/')
        self.assertEqual(found.func, homepage)