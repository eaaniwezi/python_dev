from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\pythonDev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.set_window_position(0, 0)
driver.set_window_size(1400, 900)

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_count.click()
comm_portal = driver.find_element(By.LINK_TEXT, "Community portal")
# comm_portal.click()

searches = driver.find_element(By.NAME, "search")
searches.send_keys("Python")
searches.send_keys(Keys.ENTER)


driver.quit()
