from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = "sezitoushangyibadao"
FB_PASSWORD = "sezitoushangyibadao"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

sleep(5)
login_button = driver.find_element(by=By.XPATH, value='//*[@id="t-2098970229"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

sleep(5)
fb_login = driver.find_element(by=By.XPATH, value='//*[@id="t467615991"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div/div')
fb_login.click()

sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
email.send_keys(FB_EMAIL)
password = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element(by=By.XPATH, value='//*[@id="t467615991"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location_button.click()
notifications_button = driver.find_element(by=By.XPATH, value='//*[@id="t467615991"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
notifications_button.click()
cookies = driver.find_element(by=By.XPATH, value='//*[@id="t-2098970229"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()

for n in range(100):
    sleep(2)
    try:
        print("called")
        like_button = driver.find_element(by=By.CSS_SELECTOR, value='//*[@id="t-2098970229"]/div/div[1]/div/div/main/div/div/div/div/div[4]/div/div[4]/button/span/span/svg/path')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(by=By.CSS_SELECTOR, value='.itsAMatch a')
            match_popup.click()

        except NoSuchElementException:

            sleep(2)

driver.quit()
