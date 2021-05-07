import unittest
from selenium.webdriver.support.color import Color

class Elements(unittest.TestCase):

    def header(self, driver):

        header_locator = driver.find_element_by_class_name("header")

        return header_locator

    def header_background_color(self, driver):
        header = Elements().header(driver)

        rgb_color = header.value_of_css_property("background-color")
        hex_color = Color.from_string(rgb_color).hex

        return hex_color

    def dropdown_button_background_color(self, driver):
        dropdown_button = Elements().dropdown_button(driver)

        rgb_color = dropdown_button.value_of_css_property("background-color")
        hex_color = Color.from_string(rgb_color).hex

        return hex_color

    def dropdown_button_border_color(self, driver):
        dropdown_button = Elements().dropdown_button(driver)

        dropdown_button.click()

        rgb_color = dropdown_button.value_of_css_property("border-color")
        hex_color = Color.from_string(rgb_color).hex

        return hex_color

    def dropdown_button_border_height(self, driver):
        dropdown_button = Elements().dropdown_button(driver)

        dropdown_button.click()

        border_width = dropdown_button.value_of_css_property("border-width")

        return border_width

    def logo(self, driver):

        logo_locator = driver.find_element_by_class_name("logo")

        return logo_locator

    def dropdown_button(self, driver):

        dropdown_button = driver.find_element_by_id("dropdown-button")

        return dropdown_button

    def dropdown_list(self, driver):

        dropdown_button = self.dropdown_button(driver)

        dropdown_button.click()

        dropdown_list = driver.find_element_by_class_name("optionsList")

        return dropdown_list

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

