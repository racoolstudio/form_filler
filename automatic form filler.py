from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/racool/Desktop/chromedriver'

driver = webdriver.Chrome(chrome_driver_path)
driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
first_name.send_keys('Ridwan')
last_name.send_keys('Abdulwaheed')


