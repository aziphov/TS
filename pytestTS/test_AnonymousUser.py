import random
import time
import datetime
from pytestTS.Locators.AnonymousPage import Anonymous
from pytestTS.Locators.MyTSPage import MyTS
from pytestTS.Locators.CreateProfilePage import CreateProfile
from pytestTS.Locators.ChatPage import Chat
from pytestTS.Locators.CommonLocators import Common
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome(executable_path="chromedriver.exe")
# driver.find_element_by

# @pytest.mark.usefixtures("browser")
def test_anonymous_chatting(browser):
    now = datetime.datetime.now()
    anonymous = Anonymous(browser)
    my_ts = MyTS(browser)
    create_profile = CreateProfile(browser)
    chat = Chat(browser)
    common = Common(browser)

    browser.get("https://m.pwa.tsescorts.com/alabama/akron/shemale-escorts")
    anonymous.profile_shemale().click()
    anonymous.close_homescreen().click()
    message_data_sent = now.strftime("%d-%m-%Y %H:%M") # установить текущую дату
    anonymous.profile_input_filed().send_keys(message_data_sent)
    anonymous.profile_send_button().click()
    common.allow_location_access_pop_up_ok_button().click()
    time.sleep(12)
    chat.plus_cross_button().click()
    time.sleep(1)
    file_path = "C:/Users/kiraz/PycharmProjects/TS/TA/ta_male.png"
    chat.file_input().send_keys(file_path)
    chat.send_message_button().click()
    anonymous.pop_up_skip().click()
    common.back_button().click()
    anonymous.chat_tab().click()
    chat_id = anonymous.get_dialogue_attribute()
    anonymous.login_tab().click()
    anonymous.email_or_phone_field().send_keys("+12011111117")
    anonymous.password_field_auth().send_keys("2011111117")
    anonymous.login_button().click()
    time.sleep(8)
    chat.chat_page_button().click()
    chat.dialogue(chat_id).click()
    time.sleep(3)
    message_data_received = browser.find_element_by_xpath("//div[text()='" + message_data_sent + "']")
    message_data_received.is_displayed()

