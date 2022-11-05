from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get("https://www.amazon.pl/PocketBook-czytnik-book%C3%B3w-wy%C5%9Bwietlacz-rubinowy/dp/B09QLJ6P9W/ref=sr_1_1?crid=10LVR5GJGWP5U&keywords=pocketbook+touch+lux+5&qid=1667636098&qu=eyJxc2MiOiIzLjEwIiwicXNhIjoiMy4wNiIsInFzcCI6IjIuMzIifQ%3D%3D&sprefix=pocketbook%2Caps%2C260&sr=8-1")
price=browser.find_element(By.ID, "corePrice_feature_div")
print(price.text)

browser.quit()