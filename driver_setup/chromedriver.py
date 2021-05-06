from selenium import webdriver


def chromedriver_options(*args):
    chrome_options = webdriver.ChromeOptions()

    for arg in args:
        chrome_options.add_argument(arg)

    return chrome_options

def chromedriver_setup():
    driver = webdriver.Chrome(r'/Users/hugo/PycharmProjects/unfuck_homework/selenium2 copy/driver_setup/chromedriver_90', options=chromedriver_options('-incognito', '--start-maximized', '--disable-notifications', '--disable-popup-blocking'))
    return driver
