from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
driver =webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")

class Popups:
    driver.get("https://qaboxletstestcypresspracticesite.netlify.app/differentalerttypes.html")
    def singleAlert(self):
         driver.find_element(By.ID,"alert").click() #Clicking on the button
         time.sleep(2)
         driver.switch_to.alert.accept() # We are clicking on the Ok button

    def confirmAccept(self):
         driver.find_element(By.ID,"confirm").click() #Clicking on the button
         time.sleep(2)
         Alert(driver).accept() #Alternative way to accept or click ok
         message=driver.find_element(By.TAG_NAME,"h2").text
         assert message=="CONFIRM - You pressed OK!"
    def confirmCancel(self):
         driver.find_element(By.ID,"confirm").click() #Clicking on the button
         time.sleep(2)
     #     driver.switch_to.alert.dismiss() # We are clicking on the Cancle button
         Alert(driver).dismiss() # Alternative way to click cancle
         message=driver.find_element(By.TAG_NAME,"h2").text
         assert message=="CONFIRM - You pressed Cancel!"
    def promptOk(self):
         text="ibrahim"
         driver.find_element(By.ID,"prompt").click() #Clicking on the button
         time.sleep(2)
         driver.switch_to.alert.send_keys(text) # We are entering value into the field
         time.sleep(5)
         Alert(driver).accept() #Alternative way to accept or click ok
         message=driver.find_element(By.TAG_NAME,"h2").text
         assert message=="PROMPT - Hello {}! How are you today?".format(text)

single=Popups()
single.singleAlert()

confirm=Popups()
confirm.confirmAccept()
confirm.confirmCancel()

prompt=Popups()
prompt.promptOk()