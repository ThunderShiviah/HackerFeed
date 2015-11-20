from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # I navigate to the site.
        self.browser.get('http://localhost:8000')

        # I'm greeted by HackerFeed in the title bar
        # and in the header.

        # I look down to see a list of articles.
        
        # Each article has the title

        # and the url.

        # The articles are a mix of many blogs.

        # When I hover over the article, the url becomes underlined.

        # When I click on the article, the article website opens in a new window.
        
        # The link is then marked as visited.

        # I can then press an archive button which hides that story from view and replaces it with a new one.


        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
