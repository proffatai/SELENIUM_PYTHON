from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

#LOCATING iFrame by ID of the iframe
driver.get("https://demo.automationtesting.in/Frames.html")
#in order to be able to type into that box. We need to switch contexts to iframe
driver.switch_to.frame("singleframe") # pass the ID of the iframe 
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("Hello bros")
time.sleep(5)

#LOCATING iFrame by Name of the iframe
driver.get("https://demo.automationtesting.in/Frames.html")
#in order to be able to type into that box. We need to switch contexts to iframe
driver.switch_to.frame("SingleFrame") # pass the  Name of the iframe 
driver.find_element(By.TAG_NAME, "input").send_keys("Hello bros")
time.sleep(5)

#LOCATING iFrame by XPATH of the iframe
driver.get("https://demo.automationtesting.in/Frames.html")
#in order to be able to type into that box. We need to switch contexts to iframe
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='singleframe']")) # pass the  Name of the iframe 
driver.find_element(By.TAG_NAME, "input").send_keys("Hello bros")
time.sleep(5)