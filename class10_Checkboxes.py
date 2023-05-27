from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

#Clicking on checkbox is straightforward, this is done by just clicking the checkbox
#Use is_selected() to verify if a checkbox has been selected or not


class Checkbox:
       def checkElement(self):
           driver.get("https://artoftesting.com/samplesiteforselenium")
           driver.find_element(By.CLASS_NAME,"Automation").click() 
           driver.find_element(By.CSS_SELECTOR,"input[value='Performance']").click() 
           time.sleep(5)
       def Uncheck(self):
             driver.find_element(By.CLASS_NAME,"Automation").click() #I am now unchecking the Automation option
             time.sleep(5)
       def verify (self):
             print(driver.find_element(By.CLASS_NAME,"Automation").is_selected() )
             print(driver.find_element(By.CSS_SELECTOR,"input[value='Performance']").is_selected() )
             

ob1=Checkbox() 
ob1.checkElement()

ob1.Uncheck()

ob1.verify()
