from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

EMAIL = "sezitoushangyibadao"
PASSWORD = "sezitoushangyibadao"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(5)
sign_in = driver.find_element(by=By.XPATH, value='//*[@id="t-2098970229"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
sign_in.click()

time.sleep(5)
facebook = driver.find_element(by=By.XPATH, value='//*[@id="t467615991"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div/div')
facebook.click()

time.sleep(5)
driver_facebook = webdriver.Chrome(options=chrome_options)
driver_facebook.get("https://www.facebook.com/sezitoushangyibadao")
email = driver_facebook.find_element(by=By.ID, value="email")
email.send_keys(EMAIL)
password = driver_facebook.find_element(by=By.ID, value="pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)
allow = driver.find_element(by=By.XPATH, value='//*[@id="t467615991"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow.click()
time.sleep(2)
notification = driver.find_element(by=By.XPATH, value='//*[@id="t467615991"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
notification.click()
cookie = driver.find_element(by=By.XPATH, value='//*[@id="t-2098970229"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookie.click()


for i in range(100):
    try:
        time.sleep(2)
        like = driver.find_element(by=By.CSS_SELECTOR, value="button, .Pos(r)")
        like.click()
    except NoSuchElementException as e:
        time.sleep(2)
    except ElementClickInterceptedException as e:
        back_to_tinder = driver.find_element(by=By.CSS_SELECTOR, value='.itsAMatch a')
        back_to_tinder.click()
