from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")
driver.get("https://trytestingthis.netlify.app/")
driver.maximize_window() #This is used to maximize the window
print(driver.title) #This is used to get the title of the app
time.sleep(4)
print(driver.current_url)
driver.find_element(By.LINK_TEXT,"Contact").click()
driver.fullscreen_window()
time.sleep(4)
driver.back()
driver.refresh()
time.sleep(4)
driver.forward()
time.sleep(4)
driver.minimize_window()
time.sleep(4)
# driver.quit()