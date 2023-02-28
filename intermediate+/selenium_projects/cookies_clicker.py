from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\pythonDev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.set_window_position(0, 0)
driver.set_window_size(1400, 900)



# select_lang = driver.find_element(By.ID,  "langSelect-EN")
# select_lang.click()

