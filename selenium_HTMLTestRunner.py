# coding: utf-8

import unittest
import HTMLTestRunner
from time import sleep
from selenium import webdriver
# from selenium_ActionChains import ActionChains


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.baidu.com'
        self.dr = webdriver.Firefox()
        self.dr.get(self.url)
        self.dr.implicitly_wait(20)
        self.dr.maximize_window()
        sleep(3)

    # @unittest.skip("xx")
    def test_1(self):
        test_url = "https://www.baidu.com/"
        self.assertTrue(self.dr.current_url == test_url)
        print "current url is: ", self.dr.current_url

    def test_2(self):
        self.assertNotIn('xx', self.dr.current_url)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    filename = 'd:\\Report.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='selenium',
        description=u'展示测试结果'
        )
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_1"))
    suite.addTest(MyTestCase("test_2"))
    runner.run(suite)
