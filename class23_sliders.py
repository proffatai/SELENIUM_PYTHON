from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

driver.get("https://www.snapdeal.com/")
driver.maximize_window()
object= ActionChains(driver)
mobileAccessories=driver.find_element(By.XPATH,"//span[normalize-space()='Mobile & Accessories']") #we are identifying the element we wanna locate
object.move_to_element(mobileAccessories).perform() # we wanna move the cursor to the resume writing section
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "POWER").click() #we are clicking on an element after we have hovered on resume writing menu
time.sleep(6)

#Now let us slide using drag and drop technique (METHOD 1)
source=driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
destination=driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")

object.drag_and_drop_by_offset(source, 20,0).perform() # we are draging to x axis by 20units and 0units to the y axis
time.sleep(5)

#Now let us slide using drag and drop technique (METHOD 2)
object.click_and_hold(destination).pause(1).move_by_offset(-50,0).release().perform() # we clicked and hold on the source then we waited 1 sec before moving -50units horizantally and no vertical movement, the we release(stoppped holding)
time.sleep(5)

#Now let us slide using drag and drop technique (METHOD 3)
object.move_to_element(source).pause(1).click_and_hold(source).pause(1).move_by_offset(50,0).release().perform() # we clicked and hold on the source then we waited 1 sec before moving 50units horizantally and no vertical movement
time.sleep(5)