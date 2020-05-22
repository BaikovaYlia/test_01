from selenium import webdriver
import  unittest
from selenium.webdriver.common.keys import Keys
import  time

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrom()
        self.driver.get('https://www.google.com')

        def test_01(self):
            driver = self.driver
            input_fild = driver.find_element_by_id('lst-id')
            input_fild.send_keys('python')
            input_fild.send_keys(Keys.ENTER)

            time.sleep(2)

            titles = driver.find_element_by_class_name('r')
            for title in titles:
                assert 'python' in title.text.lower()
        def teat_02(self):
            driver = self.driver
            input_fild = driver.find_element_by_id('lst-id')
            input_fild.send_keys('python')
            time.sleep(2)
            input_fild.send_keys(Keys.DOWN)
            input_fild.send_keys(Keys.ENTER)

            time.sleep(2)

            titles = driver.find_element_by_class_name('r')
            for title in titles:
                assert 'python' in title.text.lower()
        def tearDown(self):
            self.driver.quit()



