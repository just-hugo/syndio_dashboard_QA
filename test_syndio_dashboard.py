import unittest
from selenium.webdriver.support.color import Color
from driver_setup import chromedriver
from elements import elements

driver = chromedriver.chromedriver_setup()


class Syndio(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        print("setUpClass is beginning")

        driver.get("https://syndio-qa-db.herokuapp.com/")

    @classmethod
    def tearDownClass(cls):

        driver.quit()

    def setUp(self):

        print("setUp is beginning")

        driver.implicitly_wait(3)

    def tearDown(self):

        print("tearDown is beginning")

        driver.implicitly_wait(3)

        driver.refresh()

    def test_does_header_exist(self):

        header = elements.Elements().header(driver)

        driver.implicitly_wait(3)

        self.assertTrue(header.is_displayed())

    def test_does_logo_exist(self):

        logo = elements.Elements().logo(driver)

        driver.implicitly_wait(3)

        self.assertTrue(logo.is_displayed())

    def test_does_dropdown_button_exist(self):

        dropdown_button = elements.Elements().dropdown_button(driver)

        driver.implicitly_wait(3)

        self.assertTrue(dropdown_button.is_displayed())

    def test__does_dropdown_menu_exist(self):

        dropdown_button = elements.Elements().dropdown_button(driver)

        driver.implicitly_wait(3)
        dropdown_button.click()

        dropdown_list = driver.find_element_by_class_name("optionsList")

        self.assertTrue(dropdown_list.is_displayed())

    def test_does_gender_tab_exist(self):

        gender_tab = elements.Elements().gender_tab(driver)

        driver.implicitly_wait(3)

        self.assertTrue(gender_tab.is_displayed())

    def test_does_race_tab_exist(self):

        race_tab = elements.Elements().race_tab(driver)

        driver.implicitly_wait(3)

        self.assertTrue(race_tab.is_displayed())

    def test_does_pay_gap_box_exist(self):

        pay_gap = elements.Elements().pay_gap(driver)

        driver.implicitly_wait(3)

        self.assertTrue(pay_gap.is_displayed())

    def test_does_employee_comparison_box_exist(self):

        employee_comparison = elements.Elements().employee_comparison(driver)

        driver.implicitly_wait(3)

        self.assertTrue(employee_comparison.is_displayed())

    def test_does_budget_box_exist(self):

        budget = elements.Elements().budget(driver)

        driver.implicitly_wait(3)

        self.assertTrue(budget.is_displayed())

    def test_is_header_70px_high(self):

        header = elements.Elements().header(driver)

        driver.implicitly_wait(3)

        self.assertEqual(header.size["height"], 70)

    def test_is_dropdown_button_40px_high(self):

        dropdown_button = elements.Elements().dropdown_button(driver)

        driver.implicitly_wait(3)

        self.assertEqual(dropdown_button.size["height"], 40)

    def test_is_header_background_color_373737(self):

        header = elements.Elements().header(driver)

        driver.implicitly_wait(3)

        rgb_color = header.value_of_css_property("background-color")
        hex_color = Color.from_string(rgb_color).hex

        self.assertEqual(hex_color, '#373737')

    def test_is_dropdown_button_background_color_262626(self):

        dropdown_button = elements.Elements().dropdown_button(driver)

        driver.implicitly_wait(3)

        rgb_color = dropdown_button.value_of_css_property("background-color")
        hex_color = Color.from_string(rgb_color).hex

        self.assertEqual(hex_color, '#262626')

    def test_is_dropdown_button_border_color_0d8b7f_when_active(self):

        dropdown_button = elements.Elements().dropdown_button(driver)

        driver.implicitly_wait(3)
        dropdown_button.click()

        button_border_rgb = dropdown_button.value_of_css_property("border-color")
        button_border_hex = Color.from_string(button_border_rgb).hex

        self.assertEqual(button_border_hex, "#0d8b7f")

    def test_is_dropdown_button_border_1px_high_when_active(self):

        dropdown_button = elements.Elements().dropdown_button(driver)

        driver.implicitly_wait(3)
        dropdown_button.click()

        button_border = dropdown_button.value_of_css_property("border-width")

        self.assertEqual(button_border, "1px")

    def test_is_dropdown_button_clickable(self):

        dropdown_button = elements.Elements().dropdown_button(driver)

        driver.implicitly_wait(3)
        dropdown_button.click()

        button_class = dropdown_button.get_attribute("class")

        self.assertEqual(button_class, "toggle active")

    def test_is_group_by_function_menu_item_clickable(self):

        dropdown_button = elements.Elements().dropdown_button(driver)

        driver.implicitly_wait(3)
        group_by_function_option = elements.Elements().group_by_function_menu_item(driver)

        group_by_function_option.click()

        button_class = dropdown_button.get_attribute("class")

        self.assertEqual("toggle ", button_class)

    def test_is_group_by_role_menu_item_clickable(self):

        dropdown_button = elements.Elements().dropdown_button(driver)
        group_by_role_menu_item = elements.Elements().group_by_role_menu_item(driver)

        driver.implicitly_wait(3)
        group_by_role_menu_item.click()

        button_class = dropdown_button.get_attribute("class")

        self.assertEqual("toggle ", button_class)

    def test_is_gender_tab_active_by_default(self):

        gender_tab = elements.Elements().gender_tab(driver)

        driver.implicitly_wait(3)
        tab_class = gender_tab.find_element_by_tag_name("button").get_attribute("class")

        self.assertEqual("tab tab-active", tab_class)

    def test_is_race_tab_clickable(self):

        race_tab = elements.Elements().race_tab(driver)

        driver.implicitly_wait(3)
        race_tab.click()

        tab_class = race_tab.find_element_by_tag_name("button").get_attribute("class")

        self.assertEqual("tab tab-active", tab_class)

    def test_does_clicking_race_tab_repopulate_pay_gap_box(self):

        race_tab = elements.Elements().race_tab(driver)
        pay_gap = elements.Elements().pay_gap(driver)
        pay_equity_content = pay_gap.find_element_by_tag_name('p').get_attribute("innerHTML")

        driver.implicitly_wait(3)
        race_tab.click()

        repopulated_content = pay_gap.find_element_by_tag_name('p').get_attribute("innerHTML")

        self.assertNotEqual(pay_equity_content, repopulated_content)

    def test_does_clicking_race_tab_repopulate_employee_comparison_box(self):

        race_tab = elements.Elements().race_tab(driver)
        employee_comparison = elements.Elements().employee_comparison(driver)
        employee_comparison_content = employee_comparison.find_element_by_tag_name('p').get_attribute("innerHTML")

        driver.implicitly_wait(3)
        race_tab.click()

        repopulated_content = employee_comparison.find_element_by_tag_name('p').get_attribute("innerHTML")

        self.assertNotEqual(employee_comparison_content, repopulated_content)

    def test_does_clicking_race_tab_repopulate_budget_box(self):

        race_tab = elements.Elements().race_tab(driver)
        budget = elements.Elements().budget(driver)
        budget_content = budget.find_element_by_tag_name('p').get_attribute("innerHTML")

        driver.implicitly_wait(3)
        race_tab.click()

        repopulated_content = budget.find_element_by_tag_name('p').get_attribute("innerHTML")

        self.assertNotEqual(budget_content, repopulated_content)


if __name__ == '__main__':
    unittest.main()
