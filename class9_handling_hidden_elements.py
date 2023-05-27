from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

class HiddenElements:
  #This method is used when the hidden element is still available in the DOM, so we can still get a locator/selector for the element even when it is hidden     
       def checkElement(self):
           driver.get("https://w3schools.com/howto/howto_js_toggle_hide_show.asp")
           status1=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed() #Element is visible by default
           driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click() #let's hide the element
           time.sleep(5)
           status2=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
           print("status 1 is ",status1,"    status 2 is ",status2)


ob1=HiddenElements() 
ob1.checkElement()
