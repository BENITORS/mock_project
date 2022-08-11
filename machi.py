import unittest
import selenium
from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os
import time

class mockTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        opt = Options()
        opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        ser = Service('c:/chromedriver.exe')
        cls.driver = webdriver.Chrome(service=ser, options=opt)
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test1_click_over_woman_tab(self):
        driver = self.driver
        ##shorts_button = driver.find_element(By.XPATH,'//*[@id="endpoint"]/tp-yt-paper-item/yt-formatted-string[(text()="Shorts")]')
        ##shorts_button.click()
        women = driver.find_element(By.XPATH, '//a[@class="level0 has-children" and (text()="Women")]')
        women.click()
        time.sleep(3)

    def test2_click_over_accessories_tab(self):
        driver = self.driver
        accessories = driver.find_element(By.XPATH, '//a[@class="level0 has-children" and (text()="Accessories")]')
        accessories.click()
        time.sleep(3)

    def test3_sendkeys_to_searchBox(self):
        driver = self.driver
        search = driver.find_element(By.ID, 'search')
        search.send_keys('tee')
        time.sleep(3)

    def test4_click_on_search_button(self):   
        driver = self.driver
        bottonsearch = driver.find_element(By. XPATH, '//*[@class="button search-button"]')
        bottonsearch.click()
        time.sleep(3)

    def test5_newUser_register(self):
        driver = self.driver
        account = driver.find_element(By. XPATH, '//*[@class="label" and (text()="Account")]')
        account.click()
        time.sleep(3)
        Register = driver.find_element(By.XPATH, '//*[@title="Register" and (text()="Register")]')
        Register.click()
        time.sleep(3)
        Firstname = driver.find_element(By.ID, 'firstname')
        Firstname.click()
        Firstname.send_keys('Jesus')
        time.sleep(3)
        Middlename = driver.find_element(By.ID, 'middlename')
        Middlename.click()
        Middlename.send_keys('Salvador')
        time.sleep(3)
        Lastname = driver.find_element(By.ID, 'lastname')
        Lastname.click()
        Lastname.send_keys('Ruvalcaba Salazar')
        time.sleep(3)
        Email = driver.find_element(By.ID, 'email_address')
        Email.click()
        Email.send_keys('jesusruvalcaba194@gmail.com')
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        Password = driver.find_element(By.ID, 'password')
        Password.click()
        Password.send_keys('Pistache27')
        time.sleep(3)
        Confirmpassword = driver.find_element(By.ID, 'confirmation')
        Confirmpassword.click()
        Confirmpassword.send_keys('Pistache27')
        time.sleep(3)
        Signup = driver.find_element(By.ID, 'is_subscribed')
        Signup.click()
        time.sleep(2)
        Registerbutton = driver.find_element(By.XPATH, '//*[@class="button" and @title="Register"]')
        Registerbutton.click()
    
    def test6_loginyouraccount(self):
        driver = self.driver
        account2 = driver.find_element(By. XPATH, '//*[@class="label" and (text()="Account")]')
        account2.click()
        time.sleep(3)
        Login = driver.find_element(By.XPATH, '//*[@title="Log In" and (text()="Log In")]')
        Login.click()
        time.sleep(3)
        Emailaddress = driver.find_element(By. XPATH, '//*[@title="Email Address"]')
        Emailaddress.click()
        Emailaddress.send_keys('jesusruvalcaba194@gmail.com')
        time.sleep(3)
        Passwordaddress = driver.find_element(By. ID, 'pass')
        Passwordaddress.click()
        Passwordaddress.send_keys('Pistache27')
        Loginbotton = driver.find_element(By. ID, 'send2')
        Loginbotton.click()

    def test7_Change_Language(self):
        driver = self.driver
        Language = driver.find_element(By. ID, 'select-language')
        Language.click()
        SelectLenguaje = Select(driver.find_element(By. XPATH, '//*[@id="select-language"]'))
        SelectLenguaje.select_by_visible_text('French')

    
        

        









    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()
        

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reportes", report_name="reporte_pruebas", open_in_browser=True))
