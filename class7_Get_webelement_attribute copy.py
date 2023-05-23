from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")
driver.get("https://trytestingthis.netlify.app/")
driver.maximize_window() #This is used to maximize the window
attr_value=driver.find_element(By.LINK_TEXT,"Contact").get_attribute("class")

print(attr_value)