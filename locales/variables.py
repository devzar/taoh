import unittest
from selenium import webdriver
import json

url_main = 'http://theageofhappiness.com'
request = 'http://theageofhappiness.com/api/posts?allPosts=&allDrafts=&category=&authorId=&searchText=&page=1&everything=1&appLanguages=%7B%22ru%22%3Atrue%2C%22en%22%3Atrue%7D&subscription=&drafts=&changedFilters=true'

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(request)
        text_from_page = driver.find_element_by_css_selector('html>body>pre').text
        json_string = json.loads(text_from_page)
        i = 0
        #while i<=21:
        #post = ''
        for p in json_string:
            all_posts = p[u'posts']
            slug =  all_posts[u'slug']
            post_id = all_posts[u'small_id_post']

            p += 1
            driver.get(url_main + '/posts/' + slug + '/' + post_id)
            if driver.find_element_by_css_selector('h1'):
                print('article [%s] exists' % slug)
            else:
                print ('article [%s] does not exist' % slug)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
