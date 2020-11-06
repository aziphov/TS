from pytestTS.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class MyTS(BasePage):

     def add_card_button(self):
          add_card_button = self.find_element((By.XPATH, "//span[.='Add Card']"))
          return add_card_button

     def address_field(self):
          address_field = self.find_element((By.CSS_SELECTOR, "[name='address']"))
          return address_field

     def add_card_plus_button(self):
          add_card_plus_button = self.find_element((By.XPATH, "//a[.='Add card']"))
          return add_card_plus_button

     def billing_and_payment_button(self):
          billing_and_payment_button = self.find_element((By.XPATH, "//span[text()='Billing & Payment']"))
          return billing_and_payment_button

     def create_profile_button(self):
          create_profile_button = self.find_element((By.CSS_SELECTOR, "button[class*='MuiButtonBase-root'][class*='MuiButton-containedPrimary']"))
          return create_profile_button

     def city_field(self):
          city_field = self.find_element((By.CSS_SELECTOR, "[name='city']"))
          return city_field

     def continue_button(self):
          continue_button = self.find_element((By.XPATH, "//span[.='Continue']"))
          return continue_button

     def cvc_field(self):
          cvc_field = self.find_element((By.CSS_SELECTOR, "[name='csc']"))
          return cvc_field

     def country_dropdownlist(self):
          country_dropdownlist = self.find_element((By.CSS_SELECTOR, "#mui-component-select-country"))
          return country_dropdownlist

     def choose_your_payment_method_credit_card(self):
          choose_your_payment_method_credit_card = self.find_element_4_sec((By.XPATH, "//div[text()='Credit Card']"))
          return choose_your_payment_method_credit_card

     def card_number_field(self):
          card_number_field = self.find_element((By.CSS_SELECTOR, "[name='cardno']"))
          return card_number_field

     def email_field(self):
          email_field = self.find_element((By.CSS_SELECTOR, "[name='email']"))
          return email_field

     def first_name_field(self):
          first_name_field = self.find_element((By.CSS_SELECTOR, "[name='firstname']"))
          return first_name_field

     def last_name_field(self):
          last_name_field = self.find_element((By.CSS_SELECTOR, "[name='lastname']"))
          return last_name_field

     def male_checkbox(self):
          male_checkbox = self.find_element((By.XPATH, "//b[.='Male']"))
          return male_checkbox

     def month_field(self):
          month_field = self.find_element((By.CSS_SELECTOR, "[name='exp_month']"))
          return month_field

     def next_button(self):
          next_button = self.find_element((By.XPATH, "//span[.='Next']"))
          return next_button

     def pay_button(self):
          pay_button = self.find_element((By.CSS_SELECTOR, "button[class*='MuiButton-containedSecondary']"))
          return pay_button

     def remove_button(self):
          remove_button = self.find_element_4_sec((By.XPATH, "//span[.='REMOVE']"))
          return remove_button

     def remove_card_pop_up_remove_button(self):
          remove_card_pop_up_remove_button = self.find_element((By.XPATH, "//span[.='Remove']"))
          return remove_card_pop_up_remove_button

     def shemale_checkbox(self):
          shemale_checkbox = self.find_element((By.XPATH, "//b[.='Shemale']"))
          return shemale_checkbox

     def usa_country(self):
          usa_country = self.find_element((By.CSS_SELECTOR, "div[data-value='1']"))
          return usa_country

     def upgrade_to_gold_button(self):
          upgrade_to_gold_button = self.find_element((By.XPATH, "// span[. = 'Upgrade to Gold']"))
          return upgrade_to_gold_button

     def upgrade_your_membership_button(self):
          upgrade_your_membership_button = self.find_element((By.CSS_SELECTOR, "span[class*='MuiButton-startIcon'][class*='MuiButton-iconSizeMedium']"))
          return upgrade_your_membership_button

     def upgrade_your_profile_upgrade_now(self):
          upgrade_your_profile_upgrade_now = self.find_element((By.XPATH, "//b[.='Upgrade Now']"))
          return upgrade_your_profile_upgrade_now

     def upgrade_your_profile_upgrade_later(self):
          upgrade_your_profile_upgrade_later = self.find_element((By.XPATH, "///b[.='Upgrade later']"))
          return upgrade_your_profile_upgrade_later

     def verify_account_page(self):
          verify_account_page = self.find_element_4_sec((By.XPATH, "//span[.='VERIFY ACCOUNT']"))
          return verify_account_page

     def verification_upload_video_button(self):
          verification_upload_video_button = self.find_element_4_sec((By.XPATH, "//input[@id='video-upload']"))
          return verification_upload_video_button

     def visa_card(self):
          visa_card = self.find_element_4_sec((By.CSS_SELECTOR, "[alt='VISA']"))
          return visa_card

     def year_field(self):
          year_field = self.find_element((By.CSS_SELECTOR, "[name='exp_year']"))
          return year_field

     def your_saved_cards_check_box(self):
          your_saved_cards_check_box = self.find_element((By.XPATH, "//img[@alt='VISA']"))
          return your_saved_cards_check_box

     def your_payment_was_successful(self):
          your_saved_cards_check_box = self.find_element((By.XPATH, "//span[text()='Your payment was successful']"))
          return your_saved_cards_check_box

     def zip_code_field(self):
          zip_code_field = self.find_element((By.CSS_SELECTOR, "[name='zip']"))
          return zip_code_field












