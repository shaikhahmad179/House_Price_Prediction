from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Selenium Driver Setup
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Base Website - BProperty - https://www.bproperty.com
driver.get('https://www.bproperty.com/')
time.sleep(2)

# Click DropDown Button to choose between Rent or Buy
home_dropdown_btn = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/header/div[4]/div/div/div[1]/div[1]/div/div')
home_dropdown_btn.click()

# Choose either Rent or Buy
time.sleep(2)
# Buy Button
buy_dropdown = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/header/div[4]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/span[1]/button')
buy_dropdown.click()

# Rent Button
# rent_btn = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/header/div[4]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/span[2]/button')
# rent_btn.click()

done_btn = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/header/div[4]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/button[2]')
done_btn.click()

find_btn = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/header/div[4]/div/div/div[2]/a')
find_btn.click()
time.sleep(3)

root_div_tag = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/main/div[2]/div[3]/div[2]/div[1]')
list_of_property = root_div_tag.find_elements(By.CSS_SELECTOR, 'div.d6e81fd0')

list_of_json = []

for property in list_of_property:

    property_json =  {}

    price = property.find_element(By.CSS_SELECTOR, 'div.c4fc20ba')
    price = price.text

    bed_bath_sqfeet = property.find_element(By.CSS_SELECTOR, 'div._22b2f6ed')
    bed_bath_sqfeet = bed_bath_sqfeet.text

    location = property.find_element(By.CSS_SELECTOR, 'div._7afabd84')
    location = location.text

    property_json["price"] = price
    property_json["bed_bath_sqfeet"] = bed_bath_sqfeet
    property_json["location"] = location

    print(property_json)
    print('---'* 50)

    list_of_json.append(property_json)

# Terminates the driver
driver.quit()