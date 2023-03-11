import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:\pythonDev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

JOB_TITLE = "flutter"
LOGIN_CRENDENTIAL = "+ "
SUCCESSFULLY_APPLIED_JOBS = []
AVAILABLE_JOB_LIST = []
Skillset = ['Bloc','Flutter','Solid', 'OOP', 'Git',  'Dart', 'Json', 'Rest', 'Android', 'Api', 'REST API']
Skillset = [x.lower() for x in Skillset]

driver.get("https://hh.ru/")
driver.set_window_position(0, 0)
driver.set_window_size(1400, 1200)

driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div/div/div/div/div[5]/a').click()
driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/form/div[1]/fieldset/input').send_keys(LOGIN_CRENDENTIAL)
driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/form/div[4]/button[1]').click()
time.sleep(60)


driver.find_element(By.XPATH, '//*[@id="a11y-search-input"]').send_keys(JOB_TITLE)
driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div[2]/div/div/div/div/form/div/div[2]/button/span/span[2]').click()
# driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div[1]/div/div/div[2]/div/form/div/div[2]/button/span/span[2]').click()
# driver.find_element(By.NAME, 'Найти работу').click()
time.sleep(5)


#!Remove location filters
# driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div[2]/div/div[1]/div/div/form/div/div[3]/a').click()
# time.sleep(2)
# driver.find_element(By.CLASS_NAME, 'bloko-tag-button').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div[1]/form/div[31]/div[2]/button').click()

# time.sleep(5)
# get_all_listings = driver.find_elements(By.CLASS_NAME, 'vacancy-serp-item__layout') #!Get Job Description on job card


# number_of_pages = int(driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div[2]/div[2]/div[2]/div/div[5]/div/span[6]/span[3]/a').text)
# time.sleep(4)
# print(f"{number_of_pages} pages")

# while number_of_pages > 0:
#     driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div[2]/div[2]/div[2]/div/div[5]/div/a').click()
#     number_of_pages -=1

index = 0
# for i in range(1):
for i in range(3):
# for i in range(number_of_pages -1):
    get_all_listings = driver.find_elements(By.CLASS_NAME, 'serp-item__title')
    time.sleep(3)
    print(f"{len(get_all_listings)} vacancies")


    for job in get_all_listings:
        index += 1
        job_title = job.text
        job_link = job.get_attribute('href')
        job.click()
        # driver.switch_to.window(driver.window_handles[1])
        # print(f"({job_title}) {job_link}")
        AVAILABLE_JOB_LIST.append({
            "Job Title":job_title,
            "Job link":job_link
        })
        pandas.DataFrame(AVAILABLE_JOB_LIST).to_csv('avaliable_jobs_from_hh.csv')
        time.sleep(3)
        
        
                
    driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div[2]/div[2]/div[2]/div/div[5]/div/a').click()
    time.sleep(3)


# !navigate the web_driver to the open tabs 
while index > 0:
    try:
        driver.switch_to.window(driver.window_handles[index])
        current_job_title = driver.find_element(By.CLASS_NAME, 'vacancy-title')
        current_job__needed_skills = driver.find_elements(By.CLASS_NAME, 'bloko-tag-list')
        needed_skills = [skills.text.lower().strip() for skills in current_job__needed_skills]
        
        if JOB_TITLE in current_job_title.text.lower() or any(item in Skillset for item in needed_skills):
            SUCCESSFULLY_APPLIED_JOBS.append({
            "Job Title":current_job_title.text,
            "Job link":driver.current_url
        })
            driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[3]/div/div/a').click()
        # driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[3]/div/div/a').click()
            pandas.DataFrame(SUCCESSFULLY_APPLIED_JOBS).to_csv('job_result_from_hh_bot_updated_form.csv')
            time.sleep(3)
            driver.close()
            time.sleep(2)
        
        else:
            time.sleep(2)
            driver.close()
    except:
        driver.close()
        time.sleep(5)
   
        
    index -=1
    