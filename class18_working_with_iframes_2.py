from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

#LOCATING iFrame by XPATH of the iframe
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.PARTIAL_LINK_TEXT,"Iframe with in an If").click()
#in order to be able to type into that box. We need to switch contexts to iframe
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")) # pass the XPATH of the iframe (Inside the parent iframe)
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,"iframe[src='SingleFrame.html']")) #we are inside the child iframe
driver.find_element(By.TAG_NAME, "input").send_keys("Hello World in python")
time.sleep(5)

