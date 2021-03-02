# coding=UTF-8
from selenium import webdriver
from time import sleep

# 設定 driver 實例
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# 建立 driver 實例
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

# 填入 臉書信箱(手機號碼)、密碼
email = ''
password = ''

driver.get("https://www.facebook.com/")
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_name('login').click()

sleep(1)

driver.get('https://www.facebook.com/groups/464870710346711/?ref=share')