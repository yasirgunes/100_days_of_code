from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # this is the key constans of the keyboard like Enter, Shift etc.

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = driver.find_element(By.NAME, "search")  # arama kısmını buldurdum
search.send_keys("Python" + Keys.ENTER)  # yazı yazmanı sağlıyor.

python_link = driver.find_element(By.LINK_TEXT, "Python (programming language)")  # Bu yazıya sahip linki buluyor.
python_link.click()  # click methodu verilen elemana tıklıyor.


# driver.close()
