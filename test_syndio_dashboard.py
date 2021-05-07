import unittest
import functions as func
from elements import Elements as Elements

driver = func.new_driver()


class Syndio(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver.get("https://syndio-qa-db.herokuapp.com/")

    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def tearDown(self):
        driver.refresh()

    def test_does_header_exist(self):
        header = Elements().header(driver)

        self.assertTrue(header.is_displayed())

    def test_does_logo_exist(self):
        logo = Elements().logo(driver)

        self.assertTrue(logo.is_displayed())

    def test_does_dropdown_button_exist(self):
        dropdown_button = Elements().dropdown_button(driver)

        self.assertTrue(dropdown_button.is_displayed())

    def test__does_dropdown_menu_exist(self):

        dropdown_list = Elements().dropdown_list(driver)

        self.assertTrue(dropdown_list.is_displayed())

    def test_does_gender_tab_exist(self):
        gender_tab = Elements().gender_tab(driver)

        self.assertTrue(gender_tab.is_displayed())

    def test_does_race_tab_exist(self):
        race_tab = Elements().race_tab(driver)

        self.assertTrue(race_tab.is_displayed())

    def test_does_pay_gap_box_exist(self):
        pay_gap = Elements().pay_gap(driver)

        self.assertTrue(pay_gap.is_displayed())

    def test_does_employee_comparison_box_exist(self):
        employee_comparison = Elements().employee_comparison(driver)

        self.assertTrue(employee_comparison.is_displayed())

    def test_does_budget_box_exist(self):
        budget = Elements().budget(driver)

        self.assertTrue(budget.is_displayed())

    def test_is_header_70px_high(self):
        header = Elements().header(driver)

        self.assertEqual(header.size["height"], 70)

    def test_is_dropdown_button_40px_high(self):
        dropdown_button = Elements().dropdown_button(driver)

        self.assertEqual(dropdown_button.size["height"], 40)

    def test_is_header_background_color_373737(self):
        header_background = Elements().header_background_color(driver)
        self.assertEqual(header_background, '#373737')

    def test_is_dropdown_button_background_color_262626(self):
        dropdown_button_background = Elements().dropdown_button_background_color(driver)

        self.assertEqual(dropdown_button_background, '#262626')

    def test_is_dropdown_button_border_color_0d8b7f_when_active(self):
        dropdown_button_border = Elements().dropdown_button_border_color(driver)

        self.assertEqual(dropdown_button_border, "#0d8b7f")

    def test_is_dropdown_button_border_1px_high_when_active(self):
        dropdown_button_border = Elements().dropdown_button_border_height(driver)

        self.assertEqual(dropdown_button_border, "1px")

    def test_is_dropdown_button_clickable(self):
        dropdown_button = Elements().dropdown_button(driver)

        dropdown_button.click()

        button_class = dropdown_button.get_attribute("class")

        self.assertEqual(button_class, "toggle active")

    def test_is_group_by_function_menu_item_clickable(self):
        dropdown_button = Elements().dropdown_button(driver)

        group_by_function_option = Elements().group_by_function_menu_item(driver)

        group_by_function_option.click()

        button_class = dropdown_button.get_attribute("class")

        self.assertEqual("toggle ", button_class)

    def test_is_group_by_role_menu_item_clickable(self):
        dropdown_button = Elements().dropdown_button(driver)
        group_by_role_menu_item = Elements().group_by_role_menu_item(driver)

        group_by_role_menu_item.click()

        button_class = dropdown_button.get_attribute("class")

        self.assertEqual("toggle ", button_class)

    def test_is_gender_tab_active_by_default(self):
        gender_tab = Elements().gender_tab(driver)

        tab_class = gender_tab.find_element_by_tag_name("button").get_attribute("class")

        self.assertEqual("tab tab-active", tab_class)

    def test_is_race_tab_clickable(self):
        race_tab = Elements().race_tab(driver)

        race_tab.click()

        tab_class = race_tab.find_element_by_tag_name("button").get_attribute("class")

        self.assertEqual("tab tab-active", tab_class)

    def test_is_gender_tab_clickable_when_race_tab_is_active(self):
        race_tab = Elements().race_tab(driver)
        gender_tab = Elements().gender_tab(driver)

        race_tab.click()

        tab_class = gender_tab.find_element_by_tag_name("button").get_attribute("class")

        self.assertEqual("tab tab-inactive", tab_class)

    def test_does_clicking_race_tab_repopulate_pay_gap_box(self):
        race_tab = Elements().race_tab(driver)
        pay_gap = Elements().pay_gap(driver)
        pay_gap_content = pay_gap.find_element_by_tag_name('p').get_attribute("innerHTML")

        race_tab.click()

        repopulated_content = pay_gap.find_element_by_tag_name('p').get_attribute("innerHTML")

        self.assertNotEqual(pay_gap_content, repopulated_content)

    def test_does_clicking_race_tab_repopulate_employee_comparison_box(self):
        race_tab = Elements().race_tab(driver)
        employee_comparison = Elements().employee_comparison(driver)
        employee_comparison_content = employee_comparison.find_element_by_tag_name('p').get_attribute("innerHTML")

        race_tab.click()

        repopulated_content = employee_comparison.find_element_by_tag_name('p').get_attribute("innerHTML")

        self.assertNotEqual(employee_comparison_content, repopulated_content)

    def test_does_clicking_race_tab_repopulate_budget_box(self):
        race_tab = Elements().race_tab(driver)
        budget = Elements().budget(driver)
        budget_content = budget.find_element_by_tag_name('p').get_attribute("innerHTML")

        race_tab.click()

        repopulated_content = budget.find_element_by_tag_name('p').get_attribute("innerHTML")

        self.assertNotEqual(budget_content, repopulated_content)


if __name__ == '__main__':
    unittest.main()
