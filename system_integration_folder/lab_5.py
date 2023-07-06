# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.kijiji.ca/")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id", "SearchKeyword")
search_bar.send_keys("corolla")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)


# Verifying that the search results page has loaded
assert "Corolla" in driver.title


# Selecting a car from the search results
car_link = driver.find_element(By.CSS_SELECTOR, ".container-results > .search-item")
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
car_link.click()


# Waiting for the car details page to load
time.sleep(5)

# View Car picture

#car_picture = driver.find_element(By.CSS_SELECTOR, ".container-results > .search-item")

car_picture = driver.find_element(By.CSS_SELECTOR, '#mainHeroImage div[class*="generalOverlay"]')
car_picture.click()
time.sleep(5)


close_dialog = driver.find_element(By.CSS_SELECTOR, 'div[class*="overlay"] > button[class*="closeButton"]')
close_dialog.click()
time.sleep(2)


# View Seller location

# car_location = driver.find_element(By.CSS_SELECTOR, 'div[class*="locationContainer"] > a[class*="location"]')
# car_location.click()
# time.sleep(5)

# close_location_dialog = driver.find_element(By.CSS_SELECTOR,
#  'div[class="fes-pagelet"] > button[class*="closeButton"]')
# close_dialog.click()
# time.sleep(3)

# Reveal seller number

phone_reveal = driver.find_element(By.CSS_SELECTOR,
'div[class*="phoneContainer"] span[class*="revealCopy"]')
phone_reveal.click()
time.sleep(5)

phone = driver.find_element(By.CSS_SELECTOR, 'div[class*="phoneContainer"] span[class*="phoneShowNumberButton"] > span')

# confirm that seller has a contact
assert len(phone.text) == 12


#phoneShowNumberButton

#contact_seller = driver.find_element("class", "revealCopy-3312312496 revealCopyPrimary-2716345521")
#contact_seller.click()

# complete test
time.sleep(3)


# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
