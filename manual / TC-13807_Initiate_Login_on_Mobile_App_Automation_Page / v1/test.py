
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : Open https://lambdatest.com
    driver.get("https://lambdatest.com")
    driver.implicitly_wait(6)

    # Step - 2 : Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 3 : Click on the close icon
    element_locators = ["//span[@id='exit_popup_close']/img[1]", "//span[@id='exit_popup_close']/img[1]", "//span[@id='exit_popup_close']/img[1]", '#exit_popup_close > img', '#exit_popup_close > img:nth-child(1)', '#exit_popup_close > img:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 4 : Click on the 'Mobile App Automation' footer column section
    element_locators = ["//a[text()='Appium Testing']/ancestor::div[2]", "//a[text()='Appium Testing']/ancestor::div[2]", "//a[text()='Espresso Testing']/ancestor::div[2]", "//a[text()='XCUITest Testing']/ancestor::div[2]", '#footer > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4)', "//a[contains(text(),'Appium Testing')]/ancestor::div[2]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : Click on the 'Login' link
    element_locators = ["//a[text()='Login']", "//a[text()='Login']", "//a[contains(text(),'Login')]", '.chfw-header_items > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)', '.chfw-header_items > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)', "//div[contains(@class,'chfw-header_items')]/div[2]/div[1]/div[2]/a[1]", "//div[contains(@class,'chfw-header_items')]/div[2]/div[1]/div[2]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 6 : Click on the 'Enter your email' email input field
    element_locators = ["//input[@id='email-input' and @type='email']", "//input[@id='email-input' and @type='email']", '#email-input', '[placeholder="Enter your email"][type="email"]', '#email-input[placeholder="Enter your email"]', '#email-input[type="email"]', "//input[@placeholder='Enter your email' and @type='email']", "//input[contains(@placeholder,'Enter your email')]", "//div[contains(@class,'smtablet:mt-20')]/div[1]/div[3]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 7 : Type in Email Address input 'test@'
    element_locators = ["//input[@id='email-input' and @type='email']", "//input[@id='email-input' and @type='email']", '#email-input', '[placeholder="Enter your email"][type="email"]', '#email-input[placeholder="Enter your email"]', '#email-input[type="email"]', "//input[@placeholder='Enter your email' and @type='email']", "//input[contains(@placeholder,'Enter your email')]", "//div[contains(@class,'smtablet:mt-20')]/div[1]/div[3]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'test@':
            element.send_keys(char)
    else:
        element.send_keys('test@')

    driver.quit()
except Exception as e:
    driver.quit()
