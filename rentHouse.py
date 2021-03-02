from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

driver.get("https://www.facebook.com/")
driver.find_element_by_id('email').send_keys('')
driver.find_element_by_id('pass').send_keys('')
driver.find_element_by_name('login').click()

sleep(1)

driver.get('https://www.facebook.com/groups/464870710346711/?ref=share')