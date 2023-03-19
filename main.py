from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# driver2 = webdriver.Chrome(options=chrome_options)

base_url = 'https://www.bproperty.com/en/bangladesh/properties-for-sale/'
page_route = 'page-'
number_of_iter = 425

list_of_urls = []

# For 2nd page and onwards
for i in range(1, number_of_iter):

    print('Page number:', i)

    if i == 1:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.bproperty.com/en/bangladesh/properties-for-sale/')
    else:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.bproperty.com/en/bangladesh/properties-for-sale/'+page_route+str(i))

    root_div_tag = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/main/div[2]/div[3]/div[2]/div[1]')
    list_of_property_url = root_div_tag.find_elements(By.CSS_SELECTOR, 'a._287661cb')

    for url in list_of_property_url:

        href_dict = {}

        href = str(url.get_attribute('href'))
        href_dict["url"] = href
        list_of_urls.append(href_dict)

    driver.quit()

df = pd.DataFrame(list_of_urls)
df.to_csv('URL.csv', index = False)