
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time, traceback

options = UiAutomator2Options()
options.set_capability("platformName", "android")

driver = webdriver.Remote("http://localhost:4723", options=options)
try:

    def get_element(driver, locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element("xpath", locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = "xpath"
                selector = locator.get('selector', locator) if isinstance(locator, dict) else locator
                try:
                    element = driver.find_element(by_method, selector)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None
    driver.implicitly_wait(6)

    # Step - 1 : Click on 
    print('Step 1: Click on ')
    driver.implicitly_wait(6)

    # Step - 2 : Click on 
    print('Step 2: Click on ')
    driver.implicitly_wait(6)

    # Step - 3 : Click on 
    print('Step 3: Click on ')
    driver.implicitly_wait(6)

    # Step - 4 : Click on 
    print('Step 4: Click on ')
    driver.implicitly_wait(6)

    # Step - 5 : Click on 
    print('Step 5: Click on ')
    driver.implicitly_wait(6)

    # Step - 6 : Click on 
    print('Step 6: Click on ')

    driver.quit()
except Exception as e:
    driver.quit()
