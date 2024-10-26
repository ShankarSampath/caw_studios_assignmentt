import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
from pages.dynamic_table import DynamicPage
from data import config

# Define the list of JSON objects directly in the script
data = [
    {"name": "Bob", "age": 20, "gender": "male"},
    {"name": "George", "age": 42, "gender": "male"},
    {"name": "Sara", "age": 42, "gender": "female"},
    {"name": "Conor", "age": 40, "gender": "male"},
    {"name": "Jennifer", "age": 42, "gender": "female"}
]

class TestFunctionality(BaseCase):


    @pytest.mark.assignment
    def test_caw_studios_assignment(self):
        expected_data = [
            {"name": "Bob", "age": 20, "gender": "male"},
            {"name": "George", "age": 42, "gender": "male"},
            {"name": "Sara", "age": 42, "gender": "female"},
            {"name": "Conor", "age": 40, "gender": "male"},
            {"name": "Jennifer", "age": 42, "gender": "female"}
        ]

        self.get(config.URL)
        self.click(By.XPATH, DynamicPage.table_data)
        DynamicPage.update_data_in_text_box(self, data)

        for index, record in enumerate(expected_data, start=2):
            name_xpath = f"//table[@id='dynamictable']//tr[{index}]/td[1]"
            age_xpath = f"//table[@id='dynamictable']//tr[{index}]/td[2]"
            gender_xpath = f"//table[@id='dynamictable']//tr[{index}]/td[3]"

            name = self.get_text(By.XPATH, name_xpath)
            age = self.get_text(By.XPATH, age_xpath)
            gender = self.get_text(By.XPATH, gender_xpath)

            assert name == record["name"], f"Expected name {record['name']} but got {name}"
            assert age == str(record["age"]), f"Expected age {record['age']} but got {age}"
            assert gender == record["gender"], f"Expected gender {record['gender']} but got {gender}"

        allure.attach(self.driver.get_screenshot_as_png(), name='Assertion Successful',
                      attachment_type=AttachmentType.PNG)



