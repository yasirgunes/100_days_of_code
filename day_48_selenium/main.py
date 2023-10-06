from selenium import webdriver
from selenium.webdriver.common.by import By  # import By to find elements By its class Id css selector etc..
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_options = webdriver.ChromeOptions()  # we get the options of the chrome webdriver
chrome_options.add_experimental_option("detach", True)  # we added an option named detach to keep chrome open

driver = webdriver.Chrome(options=chrome_options)  # and we instantiate our driver with that options
driver.get("https://orteil.dashnet.org/cookieclicker/")  # this opens chrome

time.sleep(5)
english = driver.find_element(By.CSS_SELECTOR, "div#langSelect-EN")
english.click()

time.sleep(5)
cookie = driver.find_element(By.CSS_SELECTOR, "#cookieAnchor button")

to_buy = driver.find_elements(By.CSS_SELECTOR, ".unlocked")
duration = 300  # seconds
start_time = time.time()
timeout = time.time() + 5
wait_sec = 5

while time.time() - start_time < 1000:

    cookie.click()
    cookie_amount = int(driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split(" ")[0].replace(",", ""))
    upgrades = driver.find_elements(By.CSS_SELECTOR, "div#upgrades .enabled")

    if time.time() >= timeout:  # every 5 second past buy the most expensive we can afford
        try:
            for upgrade in upgrades:
                upgrade.click()

            to_buy = driver.find_elements(By.CSS_SELECTOR, ".unlocked.enabled")  # get the list of the unlocked products

            for item in to_buy[::-1]:  # buy the most expensive product which we can afford
                item_price = item.find_element(By.CSS_SELECTOR, ".price").text  # find the item's price

                if ',' in item_price:  # if the item_price has , like 1,000 remove the , with nothing and convert it
                    # to int.
                    item_price = int(item_price.replace(",", ""))
                else:
                    item_price = int(item_price)

                if cookie_amount >= int(item_price):  # if we can afford it buy it.
                    item.click()
        except ElementClickInterceptedException as err:
            pass

        #  Update the timeout and update the wait_sec which after that amount of time we check the products
        #  and buy things
        wait_sec *= 1.1
        timeout = time.time() + wait_sec
        print(wait_sec)
