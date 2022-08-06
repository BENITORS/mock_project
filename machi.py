from re import search
import unittest
from unittest import runner
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
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test4_nuevaprueba(self):
        driver = self.driver
        ##shorts_button = driver.find_element(By.XPATH,'//*[@id="endpoint"]/tp-yt-paper-item/yt-formatted-string[(text()="Shorts")]')
        ##shorts_button.click()
        women = driver.find_element(By.XPATH, '//a[@class="level0 has-children" and (text('')="Women")]')
        women.click()
        time.sleep(5)
    def test3_segundaprueba(self):
        driver = self.driver
        accessories = driver.find_element(By.XPATH, '//a[@class="level0 has-children" and (text('')="Accessories")]')
        accessories.click()
        time.sleep(5)
    def test1_terceraprueba(self):
        driver = self.driver
        search = driver.find_element(By.ID, 'search')
        search.send_keys('tee')
        time.sleep(5)
    def test2_buscar(self):   
        driver = self.driver
        bottonsearch = driver.find_element(By. XPATH, '//a[@class="button search-button"]')
        bottonsearch.click()
        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
        

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reportes", report_name="reporte_pruebas", open_in_browser=True))
