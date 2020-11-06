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
def test_1_tag2(browser):
    now = datetime.datetime.now()
    anonymous = Anonymous(browser)
    my_ts = MyTS(browser)
    common = Common(browser)
    chat = Chat(browser)

    anonymous.login_tab().click()
    anonymous.close_homescreen().click()
    anonymous.email_or_phone_field().send_keys("+12000000005")
    anonymous.password_field_auth().send_keys("2000000005")
    anonymous.login_button().click()
    time.sleep(5)
    common.allow_location_access_pop_up_ok_button().click()
    time.sleep(1)
    chat.chat_page_button().click()
    chat.shemale_dialogue().click()
    message_data_sent = now.strftime("%d-%m-%Y %H:%M")
    chat.input_field().send_keys(message_data_sent)
    chat.send_message_button().click()
    chat.plus_cross_button().click()
    chat.location_button().click()
    chat.share_location_button().click()
    file_path = "C:/Users/kiraz/PycharmProjects/TS/TA/ta_male.png"
    chat.file_input().send_keys(file_path)
    chat.send_message_button().click()
    common.back_button().click()
    common.hamburger_button().click()
    common.logout_button().click()
    anonymous.email_or_phone_field().send_keys("+12011111117")
    anonymous.password_field_auth().send_keys("qqqqqq")
    anonymous.login_button().click()
    time.sleep(5)
    chat.chat_page_button().click()
    chat.male_dialogue().click()
    time.sleep(3)
    message_data_received = browser.find_element_by_xpath("//div[text()='" + message_data_sent + "']")
    message_data_received.is_displayed()
