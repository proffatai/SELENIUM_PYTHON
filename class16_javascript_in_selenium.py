from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

driver.execute_script("window.open('https://www.amazon.com', '_self');") #the second argument is to make sure that the app lanches on the current tab
driver.maximize_window()
demo=driver.execute_script('return document.getElementsByTagName("input")[0];')
driver.execute_script("arguments[0].click();", demo)
time.sleep(16)