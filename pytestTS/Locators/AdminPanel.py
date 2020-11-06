from pytestTS.BaseApp import BasePage
from selenium.webdriver.common.by import By
from pytestTS.Locators.AnonymousPage import Anonymous
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Admin(BasePage):

     def profile_login_password(self, level):
          profile_login_password = self.find_element((By.CSS_SELECTOR, "tbody > tr:nth-of-type(" + level + ") > td:nth-of-type(3)")).text
          return profile_login_password

     def not_paid(self, level):
          not_paid = self.find_element((By.CSS_SELECTOR, "tbody > tr:nth-of-type(" + level + ") span:nth-of-type(2)")).text
          return not_paid





