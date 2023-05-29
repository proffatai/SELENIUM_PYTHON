from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

class autoComplete:
       def __init__(self):
           driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
           driver.find_element(By.ID,"datepicker").click()
           driver.find_element(By.LINK_TEXT, "31").click()
           
           time.sleep(5)
    
ob1=autoComplete() 


