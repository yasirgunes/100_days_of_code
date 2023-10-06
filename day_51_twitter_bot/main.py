from selenium import webdriver
from selenium.webdriver.common.by import By
import time

MY_DOWNLOAD = 100
MY_UPLOAD = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("Detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.speedtest.net/")
time.sleep(2)

# find the go button which starts the speed test and click to it.
go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
go_button.click()
time.sleep(5)

# download speed test result
test_download = int(driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                  '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
# upload speed test result
test_upload = int(driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

if MY_DOWNLOAD*0.8 > test_download or MY_UPLOAD*0.8 > test_upload:
	# go to x and complain about the service
	driver.get("")