# Readme

This test suite was built using Selenium in Python, and runs in Python's unittest framework.

## Selenium

- [https://selenium-python.readthedocs.io/](https://selenium-python.readthedocs.io/)

Selenium manipulates browsers using a Webdriver, an executable which must be downloaded and either added to your PATH or added to `driver_setup`. Then, `driver_path.py` must be updated with the PATH of your Webdriver. 

This suite was developed to run on Chrome, and your results may vary if you attempt another browser.

Locate your Chrome browser's version and then download the corresponding driver below:

- [https://selenium-python.readthedocs.io/installation.html#drivers](https://sites.google.com/a/chromium.org/chromedriver/downloads)

As an example, this test suite comes with `ChromeDriver 90.0.4430.24`, which will operate on systems running Chrome 90.0.4430

### Mac only: give access in security panel

The first time you run Selenium, it might fail to work due to being from an unidentified developer. You'll receive a warning.

[Example of the error](https://github.com/just-hugo/syndio_homework/blob/main/driver_setup/mac_webdriver_error.png?raw=true)

Go to your Mac's System Settings. In the General tab, look for the bottom section, which should have an option to `Open Anyway`

[Example of System Settings](https://github.com/just-hugo/syndio_homework/blob/main/driver_setup/mac_webdriver_solution.png?raw=true)

## Set test options

You may optionally customize browser settings (such as running incognito) or the wait time for test steps before timing out in `browser_options.py` and `wait_time.py`

## Run tests

`python -m unittest` from the project root.

## Manual QA

✅ passed manual inspection

❌ failed manual inspection

### Test cases

header exists

header height is 70 px

header background is 373737

header has logo

logo is aligned left

dropdown button exists

dropdown button is aligned right

dropdown button height is 40 px

dropdown background is 262626

dropdown button has outline when active

dropdown button active outline is 1 px

dropdown button active outline is colored 0D8B7F

dropdown button is clickable

dropdown menu has list items

dropdown list items are clickable

clicking dropdown menu items updates dashboard data

gender tab exists

gender tab is active by default

race tab exists

race tab is clickable

pay gap box exists

employee comparison box exists

budget box exists

clicking race tab repopulates content boxes

has small responsive breakpoint

has mid responsive breakpoint

has large responsive breakpoint

## Screencast

## Plans to refactor

- Expand to cross-browser support (including multiple versions of the same browser
- add functions to build a URL
