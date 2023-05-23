from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

class WebElementState:
       
       def __init__(self, *args):
           
            if len(args) == 2:
                self.username, self.password = args[0], args[1]
                driver.get("https://training.openspan.com/login")
                driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys(self.username)
                driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys(self.password)
                self.state=driver.find_element(By.ID,"login_button").is_enabled()
            else:
                 driver.get("https://training.openspan.com/login")
                 self.state=driver.find_element(By.ID,"login_button").is_enabled()
           
       def printState(self):
              
              print(self.state)
              

ob1=WebElementState("standard_user","secret_sauce") #Username and password
ob1.printState() #This should be enabled
time.sleep(5)
ob2=WebElementState("adesanmi") #username but no password
ob2.printState() # This should be disabled
time.sleep(5)
ob4=WebElementState() #no username and  no password
ob4.printState() # This should be disabled