from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")


driver.get("https://resume.naukri.com/")
object= ActionChains(driver)
resumeWriting=driver.find_element(By.CSS_SELECTOR,"a[id='rw'] span[class='gnbLabel']") #we are identifying the element we wanna locate
object.move_to_element(resumeWriting).perform() # we wanna move the cursor to the resume writing section
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Resume Samples").click() #we are clicking on an element after we have hovered on resume writing menu
time.sleep(2)