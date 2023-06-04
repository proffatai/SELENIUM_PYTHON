from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10) #This wait will apply to all the web elements. 
##The execution will wait for 10secs if the any element is not found at the point of execusion but wont wait for any sec if the element is found immediately unlike the time.sleep() that waits if or if not the element is found

driver.find_element(By.ID,"user-name").send_keys("standard_user") #app waits 10secs if the element is not found immediately
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce") #app waits 10secs if the element is not found immediately
driver.find_element(By.NAME,"login-button").click() #app waits 10secs if the element is not found immediately
time.sleep(5)