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

## Checking the state of web elements (Visible or not) <br>
We simply need to locate the element we want to get the visibility and use the is_displayed() method. `self.state=driver.find_element(By.ID,"header").is_displayed()`

<br>
### Handling multiple windows in Selenium Python<br>
Open the browser and navigate to the required page<br>
Find the current window's GuID (unique id), so we can return to this base window later<br>
Click the link/button which opens the multiple windows<br>
Get all the windows GuIDs,<br>
Remove base window ID from the above received all ids if only two windows present<br>
If more than two windows present then iterate and switch to each window and verify their title<br>
If the title matches then break the loop (iteration), so we can perform operations<br>
Close the window (optional, saves memory)<br>
Return back to the base<br>     

### Mouse over events
This can be done using the Action class. We need to import the ActionClass `from selenium.webdriver import ActionChains` then in order to use, we need to create an object of the ActionChain,`object= ActionChains(driver)` and the go ahead to use the methods available in the class.
<br>
element=driver.find_element(By.ID, "element")
`object.move_to_element(element)` is a method that can be used to over on an element but we need to chain the `.perform()` for it to execute its task

<br>
`object.context_click(element).perform()` This is to right click on the web element provided as argument. We must have stored the locator of the element inside a variable e.g element and then pass that variable as an argument to the context_click()
<br>
`object.double_click(element).perform()` this is to double click on the element provided as argument <br>

### Waits in Selenium: Implicit, Explicit and Fluent waits
NB: time.sleep(4) is a static wait in the sense that it forces the test to wait for the complete amount of time mentioned in the sleep() even if the element that is expected has been found. But for Implicit, Explicit and Fluent , they are dynamic waits and they tend to stop execution once the element that is expected to load has appeared rather than waiting for the complete time specified

<br>
Implicit wait: They are global because the wait time is applicable to all web elements within the script. This wait is used to tell the web driver to wait for some specified period of time when searching for an element(s) if they are immediately available. This wait does not require any expected condition

<br>
Explicit wait: This is used to tell the web driver to wait until either a particular condition is met or maximum time has passed.It is only applicable to the element specified by the user and not to the entire script. e.g, we can wait for a button to be enabled before we wanna continue. Such wait is an explicit wait since the driver has to wait till that button is enabled

<br>
Fluent wait: This is similar to the explicit wait. It defines the maximum amount of time to wait for a condion, as well as the frequency with which to check the condition