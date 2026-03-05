
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
    driver.implicitly_wait(6)

    # Step - 1 : open https://kaneai-playground.lambdatest.io/
    driver.get("https://kaneai-playground.lambdatest.io/")
    driver.implicitly_wait(6)

    # Step - 2 : Open new tab
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(6)

    # Step - 3 : Open https://www.google.com/search?q=amazon&oq=ama&gs_lcrp=EgZjaHJvbWUqEAgAEAAYgwEY4wIYsQMYgAQyEAgAEAAYgwEY4wIYsQMYgAQyEwgBEC4YgwEYxwEYsQMY0QMYgAQyDQgCEAAYgwEYsQMYgAQyBggDEEUYOTIKCAQQABixAxiABDIQCAUQLhjHARixAxjRAxiABDIKCAYQABixAxiABDIGCAcQBRhA0gEIMjQ1M2owajeoAgewAgHxBRUvwVmt_3L0&sourceid=chrome&ie=UTF-8
    driver.get("https://www.google.com/search?q=amazon&oq=ama&gs_lcrp=EgZjaHJvbWUqEAgAEAAYgwEY4wIYsQMYgAQyEAgAEAAYgwEY4wIYsQMYgAQyEwgBEC4YgwEYxwEYsQMY0QMYgAQyDQgCEAAYgwEYsQMYgAQyBggDEEUYOTIKCAQQABixAxiABDIQCAUQLhjHARixAxjRAxiABDIKCAYQABixAxiABDIGCAcQBRhA0gEIMjQ1M2owajeoAgewAgHxBRUvwVmt_3L0&sourceid=chrome&ie=UTF-8")
    driver.implicitly_wait(6)

    # Step - 4 : Click on the Amazon.com. Spend less. Smile more. link in search results
    element_locators = ["//h3[@id='_AzGpaYqoKNLl5NoPpN_2yAQ_17']", '#_AzGpaYqoKNLl5NoPpN_2yAQ_17', "//h3[text()='Amazon.com. Spend less. Smile more.']", '.Y6JuXb > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1) > h3:nth-child(1)', "//h3[contains(text(),'Amazon.com. Spend less. Smile more.')]", "//div[contains(@class,'Y6JuXb')]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/h3[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : switch tab to 2 index tab
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(6)

    # Step - 6 : Click on the search input box in the top center with placeholder 'Search Amazon'
    element_locators = ["//input[@id='twotabsearchtextbox']", "//input[@name='field-keywords' and @type='text']", "//input[@type='text' and @role='searchbox']", '#twotabsearchtextbox', '[name="field-keywords"][type="text"]', '[type="text"][aria-label="Search Amazon"]', '[placeholder="Search Amazon"][role="searchbox"]', '[placeholder="Search Amazon"][type="text"]', "//input[@placeholder='Search Amazon' and @aria-label='Search Amazon']", "//input[@placeholder='Search Amazon' and @type='text']", "//input[contains(@placeholder,'Search Amazon')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 7 : Type in search input field in the top center with placeholder 'Search Amazon' 'sneaker for men us polo'
    element_locators = ["//input[@id='twotabsearchtextbox']", "//input[@name='field-keywords' and @type='text']", "//input[@type='text' and @role='searchbox']", '#twotabsearchtextbox', '[name="field-keywords"][type="text"]', '[type="text"][aria-label="Search Amazon"]', '[placeholder="Search Amazon"][role="searchbox"]', '[placeholder="Search Amazon"][type="text"]', "//input[@placeholder='Search Amazon' and @aria-label='Search Amazon']", "//input[@placeholder='Search Amazon' and @type='text']", "//input[contains(@placeholder,'Search Amazon')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'sneaker for men us polo':
            element.send_keys(char)
    else:
        element.send_keys('sneaker for men us polo')
    driver.implicitly_wait(6)

    # Step - 8 : Press enter in search input field in the top center
    element_locators = ["//input[@id='twotabsearchtextbox']", "//input[@name='field-keywords' and @type='text']", "//input[@type='text' and @role='searchbox']", '#twotabsearchtextbox', '[name="field-keywords"][type="text"]', '[type="text"][aria-label="Search Amazon"]', '[placeholder="Search Amazon"][role="searchbox"]', '[placeholder="Search Amazon"][type="text"]', "//input[@placeholder='Search Amazon' and @aria-label='Search Amazon']", "//input[@placeholder='Search Amazon' and @type='text']", "//input[contains(@placeholder,'Search Amazon')]"]
    element = get_element(driver,element_locators)

    element.send_keys('ENTER')
    driver.implicitly_wait(6)

    # Step - 9 : Scroll in document
    driver.execute_script("window.scrollBy(0, 0)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 10 : Scroll in document
    driver.execute_script("window.scrollBy(0, 600)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 11 : Scroll in document
    driver.execute_script("window.scrollBy(0, 120)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 12 : Scroll in document
    driver.execute_script("window.scrollBy(0, 480)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 13 : Scroll in document
    driver.execute_script("window.scrollBy(0, 0)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 14 : Click on Add to cart button for Tommy Hilfiger Men's Pandora Sneaker
    element_locators = ["//button[@id='a-autoid-12-announce']", '#a-autoid-12-announce', '#a-autoid-12-announce[type="button"]', '#a-autoid-12-announce[aria-label="Add to cart"]', "//span[@id='a-autoid-12']/span[1]/button[1]", "//button[@id='a-autoid-12-announce' and @type='button']", "//button[@id='a-autoid-12-announce' and @aria-label='Add to cart']", '#a-autoid-12 > span:nth-child(1) > button:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
