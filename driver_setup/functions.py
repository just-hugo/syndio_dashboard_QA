from selenium import webdriver
from driver_setup import browser_options
from driver_setup.driver_path import driver_path
from driver_setup.wait_time import default_wait


# Takes a list of browser options and assigns them to webdriver.
# Options can be customized in driver_setup/browser_options.py
def chromedriver_options(options_list):
    chrome_options = webdriver.ChromeOptions()

    for arg in options_list:
        chrome_options.add_argument(arg)

    return chrome_options


# Takes strings to set webdriver path and browser options.
# Customize these settings in setup_drivers/driver_path.py and setup_options/browser_options.py
def chromedriver_setup(path, options):
    driver = webdriver.Chrome(path, options=options)

    return driver


# Initializes webdriver for test cases.
def new_driver():
    driver = chromedriver_setup(driver_path, chromedriver_options(browser_options.default_options))

    driver.implicitly_wait(default_wait)

    return driver


