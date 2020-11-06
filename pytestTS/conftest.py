import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="function")
def browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="chromedriver.exe")
    driver.set_window_size(500, 1100)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + 'i')
    driver.get("https://m.pwa.tsescorts.com/")

    time.sleep(5)
    yield driver
    time.sleep(5)
    driver.quit()


    # driver.find_element_by_xpath().get_attribute()