from re import search
import unittest
import selenium
from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time


class mockTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        opt = Options()
        opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        ser = Service('chromedriver.exe')
        cls.driver = webdriver.Chrome(service=ser, options=opt)
        driver = cls.driver
        driver.get('https://www.youtube.com/')
        driver.maximize_window()

    def test_nuevaprueba(self):
        driver = self.driver
        #shorts_button = driver.find_element(By.XPATH,'//*[@id="endpoint"]/tp-yt-paper-item/yt-formatted-string[(text()="Shorts")]')
        #shorts_button.click()
        search = driver.find_element(By.ID, 'search')
        search.send_keys('gusgri')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
