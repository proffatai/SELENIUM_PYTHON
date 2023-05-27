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

`Methods` <br>
driver.get() =Used to open url in browser <br>
driver.back() => presses the browser's back button<br>
diver.forward() => presses the browser's forward button<br>
driver.refresh() =>Refreshes the current page<br>
driver.maximize_window()<br>
driver.minimize_window()<br>
driver.fullscreen_window() => identical to pressing F11 on a windows machine<br>
driver.close() =>closes the current window<br>
driver.quit() =>closes all the windows and tabs associated with that webdriver session<br><br>

`Property`<br>
driver.current_url=>This is a property=>Used to read the current URL from the browser's address bar<br>
driver.title =Reads the current page title from the browser<br>

<br><br>
## Get the text of a web element
In order to get the text of a webelement, we need to locate the element (we can use any of the 8 methods to locate the web element first) and then use the text property. The result can be stored in a variable. <br>e.g `text=driver.find_element(By.LINK_TEXT,"Contact").text`
<br><br>
## Get value of attributes of a web element. e.g <input id=name>
id is an attribute, name is the value of the attribute, we can get the attribute value with selenium by firstly locating the element and then using the get_attribute(attrName)
<br>
e.g `attr_value=driver.find_element(By.LINK_TEXT,"Contact").get_attribute("class")` This will return the value of attr class for the element located
<br>
## Checking the state of web elements (Enabled or Disabled) <br>
We simply need to locate the element we want to get the state and use the is_enabled() method. `self.state=driver.find_element(By.ID,"login_button").is_enabled()`

## Handling Hidden Elements
