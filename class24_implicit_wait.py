from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

driver.get("https://www.saucedemo.com/")

wait=WebDriverWait(driver,10,2, ignored_exceptions=[ElementClickInterceptedException]) #I am applying a 10secs fluent wait and 2 sec poll frequency 
#the poll frequency states how frequently we want the script to check for the presence of the element or the expected condition
driver.find_element(By.ID,"user-name").send_keys("standard_user") #app waits 10secs if the element is not found immediately
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce") #app waits 10secs if the element is not found immediately

wait.until(EC.element_to_be_clickable(driver.find_element(By.NAME,"login-button"))).click() #The click action will execute with a max wait time of 10s or less if the element appears earlier

time.sleep(4)