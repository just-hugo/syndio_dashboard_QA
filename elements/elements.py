import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver_setup.functions import wait
from driver_setup import functions as func


class Elements(unittest.TestCase):

    def header(self, driver):

        header_locator = driver.find_element_by_class_name("header")

        return header_locator

    def logo(self, driver):

        logo_locator = driver.find_element_by_class_name("logo")

        return logo_locator

    def dropdown_button(self, driver):

        dropdown_button = driver.find_element_by_id("dropdown-button")

        return dropdown_button

    def group_by_function_menu_item(self, driver):

        dropdown_button = self.dropdown_button(driver)

        dropdown_button.click()

        group_by_function = driver.find_element_by_id("a9f6a4b7-d03c-4a45-b64b-791e054f36b8")

        return group_by_function

    def group_by_role_menu_item(self, driver):

        dropdown_button = self.dropdown_button(driver)

        dropdown_button.click()

        group_by_role_menu_item = driver.find_element_by_id("f1b01b57-3147-476a-a632-0c10ad2a3c1a")

        return group_by_role_menu_item

    def gender_tab(self, driver):

        gender_tab = driver.find_element_by_id('tab-gender')

        return gender_tab

    def race_tab(self, driver):

        race_tab = driver.find_element_by_id("tab-race")

        return race_tab

    def pay_gap(self, driver):

        pay_gap = driver.find_element_by_id("payEquityGap")

        return pay_gap

    def employee_comparison(self, driver):

        employee_comparison = driver.find_element_by_id("employeeComparison")

        return employee_comparison

    def budget(self, driver):

        budget = driver.find_element_by_id("budget")

        return budget

