from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        self.browser = webdriver.Firefox(firefox_binary=binary)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #User hears about a new online to-do app
        #User checks out the homepage
        self.browser.get('http://localhost:8000')

        #User notices the page  title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #User is invited to enter a to-do item

        #User types "Buy Christmas presents" into a text box

        #User hits enter, the page updates, and now the page lists
        #"1: Buy Christmas presents" as an item in a to-do list

        #There is still a text box inviting user to add another item.
        #User enter "Start Refinancing"

        #The page updates again, and now shows both items on the list

        #User wants the site to remember the list.
        #User sees the site has gererated a unique url
        #The is some explanatory text to that effect

        #User visits that url - the to do list is still there

        #User quits

if __name__ == '__main__':
    unittest.main(warnings='ignore')
