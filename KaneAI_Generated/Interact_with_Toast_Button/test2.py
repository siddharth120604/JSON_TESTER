
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
import time, traceback

options = XCUITestOptions()
options.set_capability("platformName", "ios")

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

    # Step - 1 : Click on the Toast button in the left column
    element_locators = ['//XCUIElementTypeButton[@label="Colour"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 2 : Click on the Toast button in the top left section
    element_locators = ['//XCUIElementTypeApplication[@label="Proverbial"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 3 : Click on the Toast button in the top left section
    element_locators = ['//XCUIElementTypeButton[@label="Colour"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)

    driver.quit()
except Exception as e:
    driver.quit()
