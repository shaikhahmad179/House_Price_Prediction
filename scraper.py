from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from data_preprocessing_functions import Preprocessing

# Selenium Driver Setup
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver2 = webdriver.Chrome(options=chrome_options)

# Base Website - BProperty - https://www.bproperty.com

root_div_tag = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/main.py/div[2]/div[3]/div[2]/div[1]')
list_of_property_url = root_div_tag.find_elements(By.CSS_SELECTOR, 'a._287661cb')

# for i in list_of_property_url:
#     href = i.get_attribute('href')
#
#     driver2 = webdriver.Chrome(options=chrome_options)
#     driver2.get(href)
#
#     driver2.quit()
#     print(href)

# # Preprcessing Class
# dp = Preprocessing()
#
# list_of_json = []
#
# for property in list_of_property:
#
#     property_json = {}
#
#     price = property.find_element(By.CSS_SELECTOR, 'div.c4fc20ba')
#     price = dp.price(price.text)
#     property_json["price"] = price
#
#     bed_bath_sqfeet = property.find_element(By.CSS_SELECTOR, 'div._22b2f6ed')
#     bedroom, bathroom, sq_ft = dp.get_rooms_and_size(bed_bath_sqfeet.text)
#
#     property_json["bedroom"] = bedroom
#     property_json["bathroom"] = bathroom
#     property_json["sq_ft"] = sq_ft
#
#     location = property.find_element(By.CSS_SELECTOR, 'div._7afabd84')
#     location = location.text
#
#     property_json["location"] = location
#     list_of_json.append(property_json)
#
#     # Features to add
#     # Elevators, CCTV - True or False, parking_space, furnished - True/False,.
#
# # Terminates the driver
# # driver.quit()