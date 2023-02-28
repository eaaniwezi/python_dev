from selenium import webdriver

chrome_driver_path = "C:\pythonDev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements("css selector" ,".event-widget time span")
event_names = driver.find_elements("css selector" ,".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()
