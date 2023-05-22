import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FindElements:
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    def locate_multiple_elements(self):
        #find_elements returns a list
        self.driver.get("https://www.saucedemo.com/")
        self.counter_tagName=self.driver.find_elements(By.TAG_NAME,"input") 
        self.counter_cssSelector=self.driver.find_elements(By.CSS_SELECTOR,".login_logo")
        self.counter_name=self.driver.find_elements(By.NAME,"login-button")
        self.counter_className=self.driver.find_elements(By.CLASS_NAME,"submit-button btn_action")
        self.counter_linkText=self.driver.find_elements(By.LINK_TEXT,"#password")
        self.counter_partialLinkText=self.driver.find_elements(By.PARTIAL_LINK_TEXT,"p")
        self.counter_xpath=self.driver.find_elements(By.XPATH,"//div[@class='login_logo']")
    
        time.sleep(1)
    def display_counts(self):
        print("Number of elements with input tags are",len(self.counter_tagName))
        print("Number of elements with cssSelectors attribute are ",len(self.counter_cssSelector))
        print("Number of elements with className attribute are",len(self.counter_className))
        print("Number of elements with xpath attribute are",len(self.counter_xpath))
        print("Number of elements with linkText attribute are",len(self.counter_linkText))
        print("Number of elements with partialLinkText attribute are",len(self.counter_partialLinkText))
        print("Number of elements with name attribute are",len(self.counter_name))
    
    def display_text(self): #Objective is to display all the texts for elements that has the same css_selector(.login_logo)
        
        for i in self.driver.find_elements(By.CSS_SELECTOR,".login_logo"):
            print("Elements with css selector .login_logo is(are) ", i.text)

ob=FindElements()
ob.locate_multiple_elements()
ob.display_counts()
ob.display_text()
