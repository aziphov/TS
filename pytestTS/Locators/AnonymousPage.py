from pytestTS.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Anonymous(BasePage):

     def agreeing_checkbox(self):
          agreeing_checkbox = self.find_element((By.CSS_SELECTOR, "label[class*='jss']"))
          return agreeing_checkbox

     def close_homescreen(self):
          close_homescreen = self.find_element((By.CSS_SELECTOR, "div#root > div:nth-of-type(7) div:nth-of-type(1) > button:nth-of-type(1) > span:nth-of-type(1)"))
          return close_homescreen

     def country_code_button(self):
          country_code_button = self.find_element((By.XPATH, "//div[@id='mui-component-select-phoneCode']"))
          return country_code_button

     def country_code_usa(self):
          country_code_usa = self.find_element((By.CSS_SELECTOR, "div[data-value='1#US']"))
          return country_code_usa

     def chat_tab(self):
          chat_tab = self.find_element((By.XPATH, "//span/span[text()='Chat']"))
          return chat_tab

     def create_account_button(self):
          create_account_button = self.find_element((By.XPATH, "//span[.='Create Account']"))
          return create_account_button

     def email_or_phone_field(self):
          email_or_phone_field = self.find_element((By.CSS_SELECTOR, "[name='identifier']"))
          return email_or_phone_field

     def get_dialogue_attribute(self):
          get_dialogue_attribute = self.find_element((By.XPATH, "//div[@class='d-flex px-1 py-2 nowrap undefined']")).get_attribute("chat-id")
          return get_dialogue_attribute

     def login_here_link(self):
          login_here_link = self.find_element((By.XPATH, "//a[.='login here']"))
          return login_here_link

     def login_button(self):
          login_button = self.find_element((By.XPATH, "//button/span[text()='Login']"))
          return login_button

     def login_tab(self):
          login_tab = self.find_element((By.XPATH, "//span/span[text()='Login']"))
          return login_tab

     def password_field(self):
          password_field = self.find_element((By.CSS_SELECTOR, "[name = 'password']"))
          return password_field

     def password_confirmation_field(self):
          password_confirmation_field = self.find_element((By.CSS_SELECTOR, "[name = 'password_confirmation']"))
          return password_confirmation_field

     def password_field_auth(self):
          password_field_auth = self.find_element((By.CSS_SELECTOR, "[name='password']"))
          return password_field_auth

     def phone_number_field(self):
          phone_number_field = self.find_element((By.CSS_SELECTOR, "[name='phone']"))
          return phone_number_field

     def profile_shemale(self):
          profile_shemale = self.find_element((By.CSS_SELECTOR, "[src='https://pwa.tsescorts.com/media/cache/thumb_273x273/images/p/1001531_XDPMgo_15997472829038540925323564104213.jpeg']"))
          return profile_shemale

     def profile_input_filed(self):
          profile_input_filed = self.find_element((By.XPATH, "// textarea[1]"))
          return profile_input_filed

     def profile_send_button(self):
          profile_send_button = self.find_element((By.CSS_SELECTOR, "button.test-btn-message-send .sprite-svg"))
          return profile_send_button

     def pop_up_skip(self):
          pop_up_skip = self.find_element((By.XPATH, "//span[.='Skip']"))
          return pop_up_skip

     def username_field(self):
          username_field = self.find_element((By.CSS_SELECTOR, "[name = 'username']"))
          return username_field

     def verification_code_1(self):
          verification_code_1 = self.find_element((By.CSS_SELECTOR, "div.inputs-wrapper > div:nth-of-type(1) .text-center"))
          return verification_code_1

     def verification_code_2(self):
          verification_code_2 = self.find_element((By.CSS_SELECTOR, "div.inputs-wrapper > div:nth-of-type(2) .text-center"))
          return verification_code_2

     def verification_code_3(self):
          verification_code_3 = self.find_element((By.CSS_SELECTOR, "div.inputs-wrapper > div:nth-of-type(3) .text-center"))
          return verification_code_3

     def verification_code_4(self):
          verification_code_4 = self.find_element((By.CSS_SELECTOR, "div.inputs-wrapper > div:nth-of-type(4) .text-center"))
          return verification_code_4

     def verify_button(self):
          verify_button = self.find_element((By.XPATH, "//span[.='Verify']"))
          return verify_button








