import unittest
import selenium
from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
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
        women = driver.find_element(By.LINK_TEXT, 'WOMEN')
        hover = ActionChains(driver).move_to_element(women)
        hover.perform()
        time.sleep(2)
        viewallwomen = driver.find_element(By.LINK_TEXT, 'View All Women')
        hover = ActionChains(driver).move_to_element(viewallwomen)
        hover.perform()
        viewallwomen.click()
        time.sleep(2)
        women = driver.find_element(By.LINK_TEXT, 'WOMEN')
        hover = ActionChains(driver).move_to_element(women)
        hover.perform()
        time.sleep(2)
        newarrivals = driver.find_element(By.LINK_TEXT, 'New Arrivals')
        hover = ActionChains(driver).move_to_element(newarrivals)
        hover.perform()
        newarrivals.click()
        time.sleep(2)


    def test2_click_over_Men_tab(self):
        driver = self.driver
        Men = driver.find_element(By.LINK_TEXT,'MEN')
        hover = ActionChains(driver).move_to_element(Men)
        hover.perform()
        time.sleep(2)
        viewallmen = driver.find_element(By.LINK_TEXT, 'View All Men')
        hover = ActionChains(driver).move_to_element(viewallmen)
        hover.perform()
        viewallmen.click()
        time.sleep(2)
        Men = driver.find_element(By.LINK_TEXT,'MEN')
        hover = ActionChains(driver).move_to_element(Men)
        hover.perform()
        time.sleep(2)
        Newarrivals = driver.find_element(By.LINK_TEXT, 'New Arrivals')
        hover = ActionChains(driver).move_to_element(Newarrivals)
        hover.perform()
        Newarrivals.click()
        time.sleep(2)

    def test3_Accessories_botton(self):
        driver = self.driver
        Accessories = driver.find_element(By.LINK_TEXT,'ACCESSORIES')
        hover = ActionChains(driver).move_to_element(Accessories)
        hover.perform()
        time.sleep(2)
        viewallaccesories = driver.find_element(By.LINK_TEXT, 'View All Accessories')
        hover = ActionChains(driver).move_to_element(viewallaccesories)
        hover.perform()
        viewallaccesories.click()
        time.sleep(2)
        Accessories = driver.find_element(By.LINK_TEXT,'ACCESSORIES')
        hover = ActionChains(driver).move_to_element(Accessories)
        hover.perform()
        time.sleep(2)
        Eyewear = driver.find_element(By.LINK_TEXT, 'Eyewear')
        hover = ActionChains(driver).move_to_element(Eyewear)
        hover.perform()
        Eyewear.click()
        time.sleep(2)

    def test4_homeanddecore(self):
        driver = self.driver
        homeanddecor = driver.find_element(By.LINK_TEXT,'HOME & DECOR')
        hover = ActionChains(driver).move_to_element(homeanddecor)
        hover.perform()
        time.sleep(2)
        viewallhomeanddecor = driver.find_element(By.LINK_TEXT, 'View All Home & Decor')
        hover = ActionChains(driver).move_to_element(viewallhomeanddecor)
        hover.perform()
        viewallhomeanddecor.click()
        time.sleep(2)
        homeanddecor = driver.find_element(By.LINK_TEXT,'HOME & DECOR')
        hover = ActionChains(driver).move_to_element(homeanddecor)
        hover.perform()
        time.sleep(2)
        booksandmusic = driver.find_element(By.LINK_TEXT, 'Books & Music')
        hover = ActionChains(driver).move_to_element(booksandmusic)
        hover.perform()
        booksandmusic.click()
        time.sleep(2)

    def test5_Sale_botton(self):
        driver = self.driver
        Sale = driver.find_element(By.LINK_TEXT,'SALE')
        hover = ActionChains(driver).move_to_element(Sale)
        hover.perform()
        time.sleep(2)
        viewallsale = driver.find_element(By.LINK_TEXT, 'View All Sale')
        hover = ActionChains(driver).move_to_element(viewallsale)
        hover.perform()
        viewallsale.click()
        time.sleep(2)
        Sale = driver.find_element(By.LINK_TEXT,'SALE')
        hover = ActionChains(driver).move_to_element(Sale)
        hover.perform()
        time.sleep(2)
        women = driver.find_element(By.LINK_TEXT, 'Women')
        hover = ActionChains(driver).move_to_element(women)
        hover.perform()
        women.click()
        time.sleep(2)   

    def test6_Vip_botton(self):
        driver = self.driver
        Vip = driver.find_element(By.LINK_TEXT,'VIP')
        Vip.click()
        time.sleep(2)      



    def test7_sendkeys_to_searchBox(self):
        driver = self.driver
        search = driver.find_element(By.ID, 'search')
        search.send_keys('tee')
        time.sleep(2)

    def test8_click_on_search_button(self):   
        driver = self.driver
        bottonsearch = driver.find_element(By. XPATH, '//*[@class="button search-button"]')
        bottonsearch.click()
        time.sleep(2)

    def test9_newUser_register(self):
        driver = self.driver
        account = driver.find_element(By. XPATH, '//*[@class="label" and (text()="Account")]')
        account.click()
        time.sleep(2)
        Register = driver.find_element(By.XPATH, '//*[@title="Register" and (text()="Register")]')
        Register.click()
        time.sleep(2)
        Firstname = driver.find_element(By.ID, 'firstname')
        Firstname.click()
        Firstname.send_keys('Jesus')
        time.sleep(2)
        Middlename = driver.find_element(By.ID, 'middlename')
        Middlename.click()
        Middlename.send_keys('Salvador')
        time.sleep(2)
        Lastname = driver.find_element(By.ID, 'lastname')
        Lastname.click()
        Lastname.send_keys('Ruvalcaba Salazar')
        time.sleep(2)
        Email = driver.find_element(By.ID, 'email_address')
        Email.click()
        Email.send_keys('jesusruvalcaba194@gmail.com')
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        Password = driver.find_element(By.ID, 'password')
        Password.click()
        Password.send_keys('Pistache27')
        time.sleep(2)
        Confirmpassword = driver.find_element(By.ID, 'confirmation')
        Confirmpassword.click()
        Confirmpassword.send_keys('Pistache27')
        time.sleep(2)
        Signup = driver.find_element(By.ID, 'is_subscribed')
        Signup.click()
        time.sleep(2)
        Registerbutton = driver.find_element(By.XPATH, '//*[@class="button" and @title="Register"]')
        Registerbutton.click()
    
    def test10_loginyouraccount(self):
        driver = self.driver
        account2 = driver.find_element(By. XPATH, '//*[@class="label" and (text()="Account")]')
        account2.click()
        time.sleep(2)
        Login = driver.find_element(By.XPATH, '//*[@title="Log In" and (text()="Log In")]')
        Login.click()
        time.sleep(2)
        Emailaddress = driver.find_element(By. XPATH, '//*[@title="Email Address"]')
        Emailaddress.click()
        Emailaddress.send_keys('jesusruvalcaba194@gmail.com')
        time.sleep(2)
        Passwordaddress = driver.find_element(By. ID, 'pass')
        Passwordaddress.click()
        Passwordaddress.send_keys('Pistache27')
        Loginbotton = driver.find_element(By. ID, 'send2')
        Loginbotton.click()
        time.sleep(2)

    def test11_Change_Language(self):
        driver = self.driver
        Language = driver.find_element(By. ID, 'select-language')
        Language.click()
        SelectLenguaje = Select(driver.find_element(By. XPATH, '//*[@id="select-language"]'))
        SelectLenguaje.select_by_visible_text('French')
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()
        

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reportes", report_name="reporte_pruebas", open_in_browser=True))
