import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FindElement:
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    def locate_by_id_name_css_selector(self):
        
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
        self.driver.find_element(By.NAME,"login-button").click()
        time.sleep(4)

    def locate_by_xpath_classname(self):
        self.locate_by_id_name_css_selector()
        self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        time.sleep(4)
    
    def locate_by_tagName(self):
        self.driver.get("https://trytestingthis.netlify.app/") 
        self.driver.find_element(By.TAG_NAME,"input").send_keys("Ibrahim") # it fills ibrahim into the first tag with the name `input`
        time.sleep(2)

    def link_and_partial_link_text(self):
        self.driver.get("https://trytestingthis.netlify.app/") 
        self.driver.find_element(By.LINK_TEXT,"Contact").click()
        time.sleep(2)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Hom").click() #retun back to home
        time.sleep(2)

ob=FindElement()
ob.locate_by_id_name_css_selector()
ob.locate_by_xpath_classname()
ob.locate_by_tagName()
ob.link_and_partial_link_text()