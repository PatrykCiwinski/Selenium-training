import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser=Chrome()
browser.get("https://allegro.pl/")
accept_cookies=browser.find_element(By.XPATH, '//*[@id="opbox-gdpr-consents-modal"]/div/div[2]/div/div[2]/button[1]')
accept_cookies.click()
search= browser.find_element(By.NAME,"string")
search.send_keys("orzechy")
search.send_keys(Keys.ENTER)

browser.quit()
