import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "chrome_driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

BASE_URL = "https://www.udemy.com/course/100-days-of-code/"

MY_EMAIL = " "
MY_PASSWORD = " "
TO_EMAIL = " "

driver.get(BASE_URL)
driver.set_window_position(0, 0)
driver.set_window_size(1400, 1200)


def get_course_details(driver):
    course_name = driver.find_element(
        By.XPATH, '//*[@id="udemy"]/div[1]/div[2]/div/div/div[1]/div[3]/div/div/div[3]/div/h1').text
    course_description = driver.find_element(
        By.XPATH,  '//*[@id="udemy"]/div[1]/div[2]/div/div/div[1]/div[3]/div/div/div[3]/div/div[1]').text
    course_price = driver.find_element(
        By.XPATH,  '//*[@id="udemy"]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/span[2]/span').text
    return  {
        "Course Name": course_name,
        "Course Description": course_description,
        "Course Price": course_price
    }


def send_course_details():
    result = get_course_details(driver)
    print(result)
    time.sleep(10)
    courseName = result["Course Name"]
    courseDes = result["Course Description"]
    coursePrice_encode = result["Course Price"].encode('ascii', "ignore")
    coursePrice = coursePrice_encode.decode()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL,
                            msg=f"Subject:Udemy-Notifier\n\nCOURSE NAME: {courseName}\nCOURSE DESCRIPTION: {courseDes}\nCOURSE PRICE: {coursePrice}rubles \nCheck more on the course website{BASE_URL}")



send_course_details()
driver.close()