## Getting started with Selenium with Python
Firstly install python and install selenium on cmd via `pip install selenium` proceed to vscode to create a python file

Secondly proceed to download a webdriver, say chrome webdriver for example. Search for chrome webdriver on the net and download the specific chrome version for the chrome you have on your PC. Visit the setting section and get the version number of the chrome you have on your PC before proceeding to download the chromedriver for that version

Now extract the chromedriver and store it in a know location which you will pass to the `executable_path=` arg of the webdriver.Chrome()

Now we can proceed to write our automation scripts. 

## Use of Driver Manager from pypi
This is important as it saves us the need to manually download the browser driver we need and also needing to set the path.
First thing first, we need to install the module from cmd via the command: `pip install webdriver-manager`
We can visit pypi and search for webdriver manager. Doing this, we get to see the command to include in our scripts that would automatically download the needed browser we need to run our test. See `class2_using_driver_manage.py` for the usage. 


## Finding an element via selectors
There are 8 different methods to access or locate any element on the web. All these 8 methods have been treated in `class3_finding_an_element.py` 

`time` module needs to be imported so we can access the sleep(sec) and use it to provide some delay during automation

## Finding Elements via selectors
There are also 7 methods with exception to find by ID since IDs are meant to be unique to access multiple elements with the same selector.Then a list of those elements is returned by selenium e.g `self.driver.find_elements(By.ID,"user-name").send_keys("standard_user")`

## Browser commands
This implies the command we can use to interact with the browser we are lanching via selenium script

`Methods`
driver.get() =Used to open url in browser
driver.back() => presses the browser's back button
diver.forward() => presses the browser's forward button
driver.refresh() =>Refreshes the current page
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window() => identical to pressing F11 on a windows machine
driver.close() =>closes the current window
driver.quit() =>closes all the windows and tabs associated with that webdriver session

`Property`
driver.current_url=>This is a property=>Used to read the current URL from the browser's address bar
driver.title =Reads the current page title from the browser