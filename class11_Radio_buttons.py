from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

#Clicking on radio button is straightforward, this is done by just clicking the radio button
#Use is_selected() to verify if a checkbox has been selected or not


class RadioButton:
  #This method is used when the hidden element is still available in the DOM, so we can still get a locator/selector for the element even when it is hidden     
       def checkElement(self):
           driver.get("https://artoftesting.com/samplesiteforselenium")
           driver.find_element(By.ID,"male").click() 
           time.sleep(5)
           driver.find_element(By.ID,"female").click()
           time.sleep(5)

       def verify (self):
             print(driver.find_element(By.ID,"female").is_selected() ) #I expect true since female was selected lastly
             

ob1=RadioButton() 
ob1.checkElement()


ob1.verify()
