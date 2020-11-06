from pytestTS.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Common(BasePage):

    def allow_location_access_pop_up_ok_button(self):
        allow_location_access_pop_up_ok_button = self.find_element((By.XPATH, "//span[text()='OK']"))
        return allow_location_access_pop_up_ok_button

    def back_button(self):
        back_button = self.find_element((By.CSS_SELECTOR, ".small"))
        return back_button

    def hamburger_button(self):
        hamburger_button = self.find_element((By.CSS_SELECTOR, "span[class*='MuiIconButton']"))
        return hamburger_button

    def logout_button(self):
        logout_button = self.find_element((By.XPATH, "//span[.='Logout']"))
        return logout_button

    def next_button(self):
        next_button = self.find_element((By.XPATH, "//span[.='Next']"))
        return next_button