from pytestTS.BaseApp import BasePage
from selenium.webdriver.common.by import By
from pytestTS.Locators.AnonymousPage import Anonymous
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Chat(BasePage):

     def allow_notification_receive_pop_up(self):
          allow_notification_receive_pop_up = self.find_element((By.XPATH, "//span[.='OK']"))
          return allow_notification_receive_pop_up

     def chat_page_button(self):
          chat_page_button = self.find_element((By.XPATH, "//span[text()='Chat']"))
          return chat_page_button

     def file_input(self):
          file_input = self.find_element((By.XPATH, "//input[@id='image-input']"))
          return file_input

     def dialogue(self, chat_id):
          dialogue = self.find_element((By.CSS_SELECTOR, "div[chat-id='" + chat_id + "']"))
          return dialogue

     def input_field(self):
          input_field = self.find_element((By.CSS_SELECTOR, "textarea[rows='1']"))
          return input_field

     def location_button(self):
          location_button = self.find_element((By.XPATH, "//button[.='Location']"))
          return location_button

     def plus_cross_button(self):
          plus_cross_button = self.find_element((By.CSS_SELECTOR, "svg[class*='sprite-svg medium jss']"))
          return plus_cross_button

     def send_message_button(self):
          send_message_button = self.find_element((By.CSS_SELECTOR, "button.test-btn-message-send .sprite-svg"))
          return send_message_button

     def share_location_button(self):
          share_location_button = self.find_element((By.XPATH, "//span[.='Share Location']"))
          return share_location_button

     def shemale_dialogue(self):
          shemale_dialogue = self.find_element((By.CSS_SELECTOR, "div[chat-id='5f7db5809e0d841a4fcbe2fd']"))
          return shemale_dialogue



