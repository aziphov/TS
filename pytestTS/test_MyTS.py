import random
import time
import datetime
from pytestTS.Locators.AnonymousPage import Anonymous
from pytestTS.Locators.MyTSPage import MyTS
from pytestTS.Locators.CommonLocators import Common
from pytestTS.Locators.AdminPanel import Admin
from pytestTS.Locators.CreateProfilePage import CreateProfile
from selenium.webdriver.common.keys import Keys

def test_male_verification(browser):
    now = datetime.datetime.now()
    anonymous = Anonymous(browser)
    my_ts = MyTS(browser)
    common = Common(browser)
    admin = Admin(browser)

    browser.get("https://pwa.tsescorts.com/russia/moscow/shemale-escorts?al=tsa")
    browser.get("https://pwa.tsescorts.com/admin/profile/list?f_type=dating")
    for level in range(1, 25): # поиск мейла без оплаты в админке
        login_password = admin.profile_login_password(str(level))
        if "713" in login_password and admin.not_paid(str(level)) == "(free)":
            break
        else:
            continue
    browser.get("https://m.pwa.tsescorts.com/")
    anonymous.login_tab().click()
    anonymous.email_or_phone_field().send_keys("+1" + login_password)
    anonymous.password_field_auth().send_keys(login_password)
    anonymous.login_button().click()
    time.sleep(7)
    common.allow_location_access_pop_up_ok_button().click()
    time.sleep(2)
    my_ts.verify_account_page().click()
    my_ts.verification_upload_video_button().send_keys("C:/Users/kiraz/PycharmProjects/TS/TA/video.mp4")
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    common.next_button().click()


# def test_upgrade_your_membership(browser):
#     now = datetime.datetime.now()
#     anonymous = Anonymous(browser)
#     my_ts = MyTS(browser)
#     common = Common(browser)
#     phone_number = "2033283713"
#
#     anonymous.login_tab().click()
#     anonymous.close_homescreen().click()
#     anonymous.email_or_phone_field().send_keys("+1" + phone_number)
#     anonymous.password_field_auth().send_keys(phone_number)
#     anonymous.login_button().click()
#     time.sleep(8)
#     my_ts.upgrade_your_profile_upgrade_now().click()
#     time.sleep(2)
#     common.allow_location_access_pop_up_ok_button().click()
#     my_ts.choose_your_payment_method_credit_card().click()
#     my_ts.next_button().click()
#     my_ts.add_card_plus_button().click()
#     my_ts.card_number_field().send_keys("4242424242424242")
#     my_ts.month_field().send_keys("10")
#     my_ts.year_field().send_keys("2025")
#     my_ts.cvc_field().send_keys("123")
#     my_ts.first_name_field().send_keys("Alex")
#     my_ts.last_name_field().send_keys("Test")
#     my_ts.address_field().send_keys("address")
#     my_ts.city_field().send_keys("city")
#     my_ts.zip_code_field().send_keys("123456")
#     my_ts.country_dropdownlist().click()
#     my_ts.usa_country().click()
#     r = random.randint(1, 1000)
#     my_ts.email_field().send_keys(str(r * now.minute) + "@" + str(r) + ".ru") # создание уникальной почты
#     my_ts.add_card_button().click()
#     time.sleep(10)
#     my_ts.visa_card().is_displayed()
#     my_ts.your_saved_cards_check_box().click()
#     my_ts.pay_button().click()
#     my_ts.your_payment_was_successful().is_displayed()


# def test_add_credit_card(browser):
    # now = datetime.datetime.now()
    # anonymous = Anonymous(browser)
    # my_ts = MyTS(browser)
    # common = Common(browser)
    # admin = Admin(browser)
    # browser.get("https://pwa.tsescorts.com/russia/moscow/shemale-escorts?al=tsa")
    # browser.get("https://pwa.tsescorts.com/admin/profile/list?f_type=dating")
    # for level in range(1, 25): # поиск мейла без оплаты
    #     login_password = admin.profile_login_password(str(level))
    #     if "713" in login_password and admin.not_paid(str(level)) == "(free)":
    #         break
    #     else:
    #         continue
    # browser.get("https://m.pwa.tsescorts.com/")
    # anonymous.login_tab().click()
    # anonymous.email_or_phone_field().send_keys("+1" + login_password)
    # anonymous.password_field_auth().send_keys(login_password)
    # anonymous.login_button().click()
    # time.sleep(7)
    # с.allow_location_access_pop_up_ok_button().click()
    # time.sleep(1)
    # my_ts.billing_and_payment_button().click()
    # try:
    #     my_ts.remove_button().click()
    #     my_ts.remove_card_pop_up_remove_button().click()
    # except Exception:
    #     pass
    # time.sleep(1)
    # my_ts.add_card_plus_button().click()
    # my_ts.card_number_field().send_keys("4242424242424242")
    # my_ts.month_field().send_keys("10")
    # my_ts.year_field().send_keys("2025")
    # my_ts.cvc_field().send_keys("123")
    # my_ts.first_name_field().send_keys("Alex")
    # my_ts.last_name_field().send_keys("Test")
    # my_ts.address_field().send_keys("address")
    # my_ts.city_field().send_keys("city")
    # my_ts.zip_code_field().send_keys("123456")
    # my_ts.country_dropdownlist().click()
    # my_ts.usa_country().click()
    # r = random.randint(1, 1000)
    # my_ts.email_field().send_keys(str(r*now.minute) + "@" + str(r) + ".ru")
    # my_ts.add_card_button().click()
    # my_ts.visa_card().is_displayed()
