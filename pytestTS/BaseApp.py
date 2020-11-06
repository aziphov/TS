import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_element_4_sec(self, locator):
        return WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")


    # def find_elements(driver, locator):
    #     return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    # def go_to_site(self):
    #     return self.driver.get(self.base_url)