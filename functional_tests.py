from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #User is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #User types "Buy Christmas presents" into a text box
        inputbox.send_keys('Buy Christmas presents')

        #User hits enter, the page updates, and now the page lists
        #"1: Buy Christmas presents" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy Christmas presents' for row in rows),
            "New to-do item did not appear in table"
        )

        #There is still a text box inviting user to add another item.
        #User enter "Start Refinancing"
        self.fail('Finish the test!')

        #The page updates again, and now shows both items on the list

        #User wants the site to remember the list.
        #User sees the site has gererated a unique url
        #The is some explanatory text to that effect

        #User visits that url - the to do list is still there

        #User quits

if __name__ == '__main__':
    unittest.main(warnings='ignore')
