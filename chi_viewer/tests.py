from django.test import TestCase

from django.core.urlresolvers import resolve
from django.test import TestCase
from chi_viewer.views import home

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

        def test_there_are_postings_in_home_page_list(self):
        	pass

        def test_can_add_postings_to_database(self):
        	pass
        	#mocking?