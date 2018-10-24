

from selenium import webdriver

class FFtests():

    def testMethod(self):
    #    driver = webdriver.Chrome(executable_path="C:\\work\\selenium_python\\chromedriver_win32\\chromedriver.exe")
    #    driver.get("www.google.com")

    #   driverlocation="C:\\work\\selenium_python\\chromedriver_win32\\chromedriver.exe"
    #   os.environ[webdriver.chrome.driver] = driverlocation
    #   driver = webdriver.Chrome(driverlocation)
    #   driver.get()

        driver =  webdriver.Firefox()
        driver.get("https://www.google.com")


ff = FFtests()
ff.testMethod()