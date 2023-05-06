import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


EMAIL = "eaaninwezi@gmail.com"
PASSWORD = ""

JOB_TITLE = "flutter"

chrome_driver_path = "C:\pythonDev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3486586183&f_AL=true&geoId=101165590&keywords={JOB_TITLE}&location=United%20Kingdom&refresh=true&sortBy=R")
driver.set_window_position(0, 0)
driver.set_window_size(1400, 900)

'''LOGIN'''
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()
time.sleep(2)
input_email = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(EMAIL)
input_password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

'''SEARCH FOR JOB'''
all_listings = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')
print(len(all_listings))

for listing in all_listings:
    print("Called")
    listing.click()
    time.sleep(2)
