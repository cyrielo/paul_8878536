import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Setting up the webdriver
driver = webdriver.Chrome()

# clear cookies from previous session
driver.delete_all_cookies()

# Navigating to Xbox homepage
driver.get("https://www.xbox.com/en-CA")
time.sleep(3)

# Open the game menu
gameMenu = driver.find_element("id", "c-shellmenu_61")
gameMenu.click()
time.sleep(5)

# Select console games
consoleGameMenu = driver.find_element("id", "shellmenu_63")
consoleGameMenu.click()
time.sleep(5)
# Select the first game

# SearchProductGrid-module__container___jew-i > li a

first_game = driver.find_element(By.CSS_SELECTOR, ".SearchProductGrid-module__container___jew-i > li a")
first_game.click()
time.sleep(5)
#Add game to cart

add_cart = driver.find_element(By.CSS_SELECTOR, ".ButtonWithFlyout-module__buttonContainer___DM0Hd + div > button")
add_cart.click()
time.sleep(5)
#view shopping cart

viewCart = driver.find_element("id", "uhf-shopping-cart")
viewCart.click()
time.sleep(5)

#process checkout


iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]

driver.switch_to.frame(iframe)

checkout = driver.find_element("id", 'store-cart-root')
checkout.click()
time.sleep(5)

driver.switch_to.default_content()




# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
# hello world
