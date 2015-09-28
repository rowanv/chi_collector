from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_a_posting(self):
        # Come to check out portfolio home page
        self.browser.get('http://localhost:8000/')

        #see that the title mentiosn portfolio
        self.assertIn('Chi', self.browser.title)

        self.fail('Finish the test')
