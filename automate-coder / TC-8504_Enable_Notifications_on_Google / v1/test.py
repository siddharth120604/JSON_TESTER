
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

    # Step - 1 : Open https://www.google.com/search?q=google+login&oq=google+logi&gs_lcrp=EgZjaHJvbWUqCggAEAAYsQMYgAQyCggAEAAYsQMYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDIKCAQQABixAxiABDIHCAUQABiABDIHCAYQABiABDIGCAcQBRhAqAIAsAIB&sourceid=chrome&ie=UTF-8&sei=eq_gaYCrMrON4-EP_eDM6AE
    driver.get("https://www.google.com/search?q=google+login&oq=google+logi&gs_lcrp=EgZjaHJvbWUqCggAEAAYsQMYgAQyCggAEAAYsQMYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDIKCAQQABixAxiABDIHCAUQABiABDIHCAYQABiABDIGCAcQBRhAqAIAsAIB&sourceid=chrome&ie=UTF-8&sei=eq_gaYCrMrON4-EP_eDM6AE")
    driver.implicitly_wait(6)

    # Step - 2 : Click on Step 1 'Enable Notification' label in left side vertical stepper
    element_locators = ["//h3[@id='_e6_gaeLYE_KJ4-EPtLil4AI_51']", '#_e6_gaeLYE_KJ4-EPtLil4AI_51', "//div[@id='rso']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/h3[1]", '#rso > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1) > h3:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 3 : Type in email or phone input field 'test@gmail.com'
    element_locators = ["//input[@id='identifierId' and @name='identifier']", "//input[@name='identifier' and @type='email']", '#identifierId', '[name="identifier"][type="email"]', '[type="email"][aria-label="Email or phone"]', '[type="email"]', "//input[@type='email' and @aria-label='Email or phone']", "//input[starts-with(@type,'email')]", '.ToAxb > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)', "//input[contains(@type,'email')]", "//div[contains(@class,'rFrNMe') and contains(@class,'X3mtXb') and contains(@class,'UOsO2') and contains(@class,'ToAxb') and contains(@class,'zKHdkd') and contains(@class,'sdJrJc') and contains(@class,'u3bW4e')]/div[1]/div[1]/div[1]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'test@gmail.com':
            element.send_keys(char)
    else:
        element.send_keys('test@gmail.com')

    driver.quit()
except Exception as e:
    driver.quit()
