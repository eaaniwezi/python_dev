import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:\pythonDev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

JOB_TITLE = "flutter"
LOGIN_CRENDENTIAL = "+79509697254"
Skillset = ['Bloc','Flutter','Solid', 'OOP', 'Git',  'Dart', 'Json', 'Rest', 'Android', ]
Skillset = [x.lower() for x in Skillset]

driver.get("https://hh.ru/")
driver.set_window_position(0, 0)
driver.set_window_size(1400, 900)

driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div/div/div/div/div[5]/a').click()
driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/form/div[1]/fieldset/input').send_keys(LOGIN_CRENDENTIAL)
driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/form/div[4]/button[1]').click()
time.sleep(60)


driver.find_element(By.XPATH, '//*[@id="a11y-search-input"]').send_keys(JOB_TITLE)
driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div[2]/div/div/div/div/form/div/div[2]/button/span/span[2]').click()
# driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div[1]/div/div/div[2]/div/form/div/div[2]/button/span/span[2]').click()
# driver.find_element(By.NAME, 'Найти работу').click()
time.sleep(2)

# get_all_listings = driver.find_elements(By.CLASS_NAME, 'vacancy-serp-item__layout') #!Get Job Description on job card
get_all_listings = driver.find_elements(By.CLASS_NAME, 'serp-item__title')
# get_all_listings = driver.find_elements(By.CSS_SELECTOR, '.bloko-header-section-3')
print(f"{len(get_all_listings)} vacancies")

index = 0
for job in get_all_listings:
    index += 1
    job_title = job.text
    job_link = job.get_attribute('href')
    print(f"{index} ({job_title}){job_link}\n")
    job.click()
    # !navigate the web_driver


while index > 0:
    driver.switch_to.window(driver.window_handles[index])
    current_job_title = driver.find_element(By.CLASS_NAME, 'vacancy-title')
    current_job__needed_skills = driver.find_elements(By.CLASS_NAME, 'bloko-tag-list')
    needed_skills = [skills.text.lower().strip() for skills in current_job__needed_skills]
    print(needed_skills)
    # current_job_title = driver.find_element(By.CLASS_NAME, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/div[1]/h1')
    # print(current_job_title.text.lower().split())
    if JOB_TITLE in current_job_title.text.lower() or any(item in Skillset for item in needed_skills):
        print(f"{current_job_title.text}\n")
        driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[3]/div/div/a').click()
    else:
        driver.close()
    index -=1
    


    # Откликнуться