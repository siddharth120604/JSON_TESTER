
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
    driver.implicitly_wait(6)

    # Step - 1 : open https://kaneai-playground.lambdatest.io/
    driver.get("https://kaneai-playground.lambdatest.io/")
    driver.implicitly_wait(6)

    # Step - 2 : Wait 1 s
    time.sleep(int(1))
    driver.implicitly_wait(6)

    # Step - 3 : Wait 2 s
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 4 : Execute JavaScript snippet
    JS_Response=driver.execute_script('''return (function(){try{return (function(){
    const a = "b"
    })()}catch(e){return {error: e.stack}}})()''')
    print("Your response is => ",JS_Response)
    driver.implicitly_wait(6)

    # Step - 5 : Execute JavaScript snippet
    JS_Response=driver.execute_script('''return (function(){try{return (function(){
    //Variables start
    const javascript_output_20260212184944_zycx = "null"
    //Variables end
    const a ="x"
    })()}catch(e){return {error: e.stack}}})()''')
    print("Your response is => ",JS_Response)

    driver.quit()
except Exception as e:
    driver.quit()
