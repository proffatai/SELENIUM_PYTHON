from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

driver.get("https://demo.automationtesting.in/Windows.html")
base_handle=driver.current_window_handle #used to hold the handle of the parent page or base page
driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
driver.close() #close the parent window. Note we have not switched handler to the new window we are on
# Now let's find all new handles (all the tabs) that are present
all_handles=driver.window_handles #stores all handles / tabs present. It will hold two values (since two tabs would be open)
for handle in all_handles:
    if (handle!=base_handle): #if the handle is not the same as the stored / base page, the we want to switch to the new handle(tab)
        driver.switch_to.window(handle) #this is to switch to the new tab
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Blog").click()
        time.sleep(2)
        break

driver.find_element(By.LINK_TEXT,"Watch the Videos").click() #opening another tab
driver.close() #Close current handler, note we have not yet switched tabs
all_latest_handles=driver.window_handles
for handle in all_latest_handles:
    if handle not in all_handles:
        driver.switch_to.window(handle) #this is to switch to the new tabs
        driver.maximize_window()
        driver.find_element(By.NAME,"search_query").send_keys("Hello world")
        driver.find_element(By.ID,"search-icon-legacy").click()
        time.sleep(5)
print(base_handle) 
print(all_handles)
print(all_latest_handles)