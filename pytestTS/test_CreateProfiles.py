import random
import time
import datetime
from pytestTS.Locators.AnonymousPage import Anonymous
from pytestTS.Locators.MyTSPage import MyTS
from pytestTS.Locators.CreateProfilePage import CreateProfile
from selenium.webdriver.common.keys import Keys
from pytestTS.Locators.CommonLocators import Common


# @pytest.mark.usefixtures("browser")
def test_create_shemale_or_male_profile(browser):
    user = "male" # выбрать male или shemale, кого именно нужно создать
    anonymous = Anonymous(browser)
    my_ts = MyTS(browser)
    create_profile = CreateProfile(browser)
    common = Common(browser)

    anonymous.close_homescreen().click()
    anonymous.login_tab().click()
    anonymous.create_account_button().click()
    anonymous.country_code_button().click()
    anonymous.country_code_usa().click()
    i = 1
    while i == 1: # получить номер телефона, который ранее не использовался
        phone_number = "2"
        for i in range(6):
            r = random.randint(0, 9)
            phone_number = phone_number + str(r)
        phone_number = phone_number + "713" # ключ, по которому можно юзера в админке
        anonymous.phone_number_field().send_keys(Keys.CONTROL,"a", Keys.DELETE)
        anonymous.phone_number_field().send_keys(phone_number)
        anonymous.username_field().send_keys(Keys.CONTROL,"a", Keys.DELETE)
        anonymous.username_field().send_keys(phone_number)
        time.sleep(2)
        try:
            login_here_link = browser.find_element_by_xpath("//a[.='login here']")
        except Exception:
            i = 2
    anonymous.password_field().send_keys(phone_number)
    anonymous.password_confirmation_field().send_keys(phone_number)
    anonymous.agreeing_checkbox().click()
    anonymous.create_account_button().click()
    anonymous.verification_code_1().send_keys("1")
    anonymous.verification_code_2().send_keys("1")
    anonymous.verification_code_3().send_keys("1")
    anonymous.verification_code_4().send_keys("1")
    anonymous.verify_button().click()
    time.sleep(3)
    my_ts.create_profile_button().click()
    if user == "male":
        my_ts.male_checkbox().click()
    else:
        my_ts.shemale_checkbox().click()
    my_ts.continue_button().click()
    common.allow_location_access_pop_up_ok_button().click()
    create_profile.name_field().send_keys(phone_number)
    create_profile.select_state_droplist().click()
    create_profile.select_state_alabama_droplist().click()
    create_profile.select_city_akron_droplist().click()
    common.next_button().click()
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    common.next_button().click()
    create_profile.tagline_field().send_keys(phone_number)
    time.sleep(1)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']"))
    browser.find_element_by_css_selector(".cke_editable").send_keys(phone_number)
    browser.switch_to.default_content()
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    common.next_button().click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    common.next_button().click()
    if user == "male": # выбор аватара для профиля
        file_path = "C:/Users/kiraz/PycharmProjects/TS/TA/ta_male.png"
    else:
        file_path = "C:/Users/kiraz/PycharmProjects/TS/TA/ta_shemale.png"
    create_profile.file_input().send_keys(file_path)
    common.next_button().click()
    if user == "male":
        my_ts.upgrade_to_gold_button().is_displayed()
    else:
        my_ts.upgrade_your_profile_upgrade_now().is_displayed()

