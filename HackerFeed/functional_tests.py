from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_view_and_visit_list_of_articles(self):

        # I navigate to the site.
        self.browser.get('http://localhost:8000')

        # I'm greeted by HackerFeed in the title bar     
        self.assertIn('HackerFeed', self.browser.title), 'HackerFeed not in browser title'

        # and in the header.

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('HackerFeed', header_text)

        # Below the header I see a list of articles.
        feed_list = self.browser.find_element_by_id('feed')
        rows = feed_list.find_elements_by_tag_name('a')
        
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
