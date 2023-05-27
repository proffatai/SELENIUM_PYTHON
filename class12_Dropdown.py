from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

#Clicking on radio button is straightforward, this is done by just clicking the radio button
#Use is_selected() to verify if a checkbox has been selected or not


class DropDown_singleSelect:
       def __init__(self):
           driver.get("https://artoftesting.com/samplesiteforselenium")
           dropDownElement=driver.find_element(By.ID,"testingDropdown")
           self.selectDD =Select(dropDownElement)
          #  time.sleep(5)
          
       def select(self):
             self.selectDD.select_by_visible_text("Database Testing")
             time.sleep(3)
             self.selectDD.select_by_index(1)
             time.sleep(3)
             self.selectDD.select_by_value("Manual")
             time.sleep(3)

class DropDown_multiSelect:
       def __init__(self):
           driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
           dropDownElement=driver.find_element(By.NAME,"multipleselect[]")
           self.selectDD =Select(dropDownElement)
          #  time.sleep(5)
          
       def multiSelect(self):
             self.selectDD.select_by_visible_text("Selenium")
             time.sleep(3)
             self.selectDD.select_by_index(0)
             time.sleep(3)
             self.selectDD.select_by_value("msmanual")
             time.sleep(3)
             self.selectDD.deselect_all()
             time.sleep(3)
             self.selectDD.select_by_index(2)
             time.sleep(3)
             self.selectDD.deselect_by_index(2)
             time.sleep(3)
ob1=DropDown_singleSelect() 
ob1.select()

ob2=DropDown_multiSelect() 
ob2.multiSelect()
