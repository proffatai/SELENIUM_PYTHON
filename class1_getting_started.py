from selenium import webdriver

#Launching the app with Chrome browser
driver=webdriver.Chrome(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")
driver.get("https://trytestingthis.netlify.app/")
driver.maximize_window() #This is used to maximize the window
print(driver.title) #This is used to get the title of the app
driver.quit()

#Now we wanna lanch another app using the Edge browser

driver=webdriver.Edge(executable_path="C:\\Users\\Ibrahim F A\\Documents\\SELENIUM PYTHON\\BrowserDrivers")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)