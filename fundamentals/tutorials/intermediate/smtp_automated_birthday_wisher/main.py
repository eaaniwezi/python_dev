##################### Normal Starting Project ######################
import random
import smtplib
import pandas
from datetime import datetime

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
my_email = ""
my_password = ""

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthdays_person['email'],
                            msg=f"Subject:Happy Birthday!!\n\n{contents}")
