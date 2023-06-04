from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

driver.get("https://jqueryui.com/droppable/")
#The element we want to drag is inside an iframe so we need to enter the iframe before locating the element
my_frame=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']") #locating the iframe
driver.switch_to.frame(my_frame) #entering the iframe
source=driver.find_element(By.ID,"draggable")
destination=driver.find_element(By.ID,"droppable")

object=ActionChains(driver)
# object.drag_and_drop(source,destination).perform() # alternaive method is shown below

object.drag_and_drop_by_offset(source, 190,92).perform()
time.sleep(5)