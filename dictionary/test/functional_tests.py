from selenium import webdriver
import unittest

class DictionaryUITest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000/dictionary')
        self.assertIn('linguipedia', self.browser.title)
        #self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')