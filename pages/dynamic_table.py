import json
import time
from os import times

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class DynamicPage(BaseCase):

    table_data = "//*[text()='Table Data']"
    existing_data = "//*[@id='jsondata']"
    refresh_table = "//*[@id='refreshtable']"

    def update_data_in_text_box(self, data):
        self.click(By.XPATH, DynamicPage.existing_data)
        self.clear(By.XPATH, DynamicPage.existing_data)
        json_data = json.dumps(data)
        self.send_keys(By.XPATH, json_data, DynamicPage.existing_data)
        self.click(By.XPATH, DynamicPage.refresh_table)
        time.sleep(5)