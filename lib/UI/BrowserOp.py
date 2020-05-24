from selenium import webdriver
from hyrobot.common import GSTORE, INFO


def open_browser():
    print('打开浏览器')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    GSTORE['global_webdriver'] = driver
    return driver


def get_global_webdriver():
    return GSTORE['global_webdriver']
