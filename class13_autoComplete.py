from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

class autoComplete:
       def __init__(self):
           driver.get("https://www.jumia.com.ng/")
           searchField=driver.find_element(By.ID,"fi-q")
           searchField.send_keys("techno phones")
           searchField.send_keys(Keys.ENTER)
           time.sleep(5)
        
ob1=autoComplete() 


