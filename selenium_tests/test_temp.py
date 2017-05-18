from selenium import webdriver
import time

from ._test_runner import TestCase
from .credentials import *


class MyTests(TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def tearDown(self):
        self.driver.quit()

    def test_some(self):
        self.driver.get(URL)
        time.sleep(5)
        assert 1==2

