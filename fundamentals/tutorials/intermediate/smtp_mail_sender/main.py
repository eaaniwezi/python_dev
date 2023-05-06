import smtplib
import random
import datetime as dt


now = dt.datetime.now()
weekday = now.weekday()
my_email = " "
my_password = " "
to_email = " "

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:Daily Quote\n\n{quote}")
