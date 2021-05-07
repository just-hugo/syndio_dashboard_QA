from selenium import webdriver
from driver_setup import browser_options
from driver_setup.driver_path import driver_path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.common.by import By


# Takes a list of browser options and assigns them to webdriver.
# Options can be customized in driver_setup/browser_options.py
def chromedriver_options(options_list):
    chrome_options = webdriver.ChromeOptions()

    for arg in options_list:
        chrome_options.add_argument(arg)

    return chrome_options


# Takes strings to set webdriver path and browser options.
# Customize driver settings in setup_drivers/driver_path.py and setup_options/browser_options.py
def chromedriver_setup(driver_path, browser_options):
    driver = webdriver.Chrome(driver_path, options=browser_options)

    return driver


# Initializes webdriver for test cases.
def new_driver():
    driver = chromedriver_setup(driver_path, chromedriver_options(browser_options.default_options))

    driver.implicitly_wait(3)

    return driver

def set_wait_time_seconds():
    return


# selector_type must be the first half of a By tuple, which follows the format of "By.ID" or "By.CLASS_NAME"
# selector must be a string of the element's attribute you've chosen to search by.
def wait_for_element(driver, selector_type, selector):
    element = wait(driver, 3).until(EC.presence_of_element_located((selector_type, selector)))

    return element
