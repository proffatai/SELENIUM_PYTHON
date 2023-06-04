from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
element=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']") #this is the element we wanna right click on
object=ActionChains(driver)
object.context_click(element).perform() # context click is used to used to right click
time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click() #click the copy option after right clicking
driver.switch_to.alert.accept() #clicking the Ok button from the alert box
time.sleep(4)

## Let's double click on the next element
double=driver.find_element(By.TAG_NAME,"button")
object.double_click(double).perform()
time.sleep(2)
driver.switch_to.alert.accept() #clicking the Ok button from the alert box
time.sleep(2)