from pytestTS.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class CreateProfile(BasePage):

     def file_input(self):
          file_input = self.find_element((By.XPATH, "//input[@id='image-upload']"))
          return file_input

     def name_field(self):
          name_field = self.find_element((By.XPATH, "//input[@name='name']"))
          return name_field

     def spoken_languages_droplist(self):
          spoken_languages_droplist = self.find_element((By.XPATH, "//div[@id='mui-component-select-languages']"))
          return spoken_languages_droplist

     def spoken_languages_english_droplist(self):
          spoken_languages_english_droplist = self.find_element((By.CSS_SELECTOR, "div[data-value='2']"))
          return spoken_languages_english_droplist

     def spoken_languages_ok_droplist(self):
          spoken_languages_ok_droplist = self.find_element((By.XPATH, "//span[.='OK']"))
          return spoken_languages_ok_droplist

     def select_state_droplist(self):
          select_state_droplist = self.find_element((By.XPATH, "//select[@name='state']"))
          return select_state_droplist

     def select_state_alabama_droplist(self):
          select_state_alabama_droplist = self.find_element((By.XPATH, "//option[.='Alabama']"))
          return select_state_alabama_droplist

     def select_city_akron_droplist(self):
          select_city_akron_droplist = self.find_element((By.XPATH, "//option[.='Akron']"))
          return select_city_akron_droplist

     def tagline_field(self):
          tagline_field = self.find_element((By.XPATH, "//input[@name='tagline']"))
          return tagline_field



