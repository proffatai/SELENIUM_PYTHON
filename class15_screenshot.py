from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

driver.get("https://www.amazon.com")
#Basically, we can take screenshots at any point in time on our web automation by calling the screenshot method
driver.get_screenshot_as_file(".//homescreen.png") # the first . in the file name implies we want it in the current directory
search=driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("shirt")
time.sleep(3)
search.screenshot(".//after_search.png") #we are taking screenshot of the element we are pointing at
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(3)   
driver.save_screenshot("..//results.png") #.. implies we going to the location outside the current directory to store our result
