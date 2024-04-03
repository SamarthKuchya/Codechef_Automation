
# Importing all required files

from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key,Controller
import time

# Get username and password from login.txt file

with open ('login.txt','r') as f:
    data=f.readlines()
    idx=data[0].find('\'')
    user=data[0][idx+1:-2]
    idx=data[1].find('\'')
    pswd=data[1][idx+1:-1]
# print(username)
# print(password)

# keyboard=Controller()
browser=webdriver.Chrome()
browser.maximize_window()

# opening and log in

browser.get('https://codechef.com')
browser.get('https://www.codechef.com/login?destination=/')
time.sleep(4)
username=browser.find_elements(By.ID,'edit-name')[1]
username.send_keys(user)
password=browser.find_elements(By.ID,'edit-pass')[1]
password.send_keys(pswd)
login_button=browser.find_elements(By.ID,'edit-submit-button')[1].click()
time.sleep(3)

# opening problem page

browser.get('https://www.codechef.com/practice')
browser.get('https://www.codechef.com/practice-old')
browser.get('https://www.codechef.com/problems/FOODCOST')
time.sleep(3)

# Uploading Code
code=browser.find_element(By.CLASS_NAME,'_upload_code_afrs9_122').click()
time.sleep(3)
keyboard=Controller()
keyboard.type('D:\\Skills\\Project Automating Codechef\\code.cpp')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# Running and submitting code

run=browser.find_element(By.XPATH,'//*[@id="compile_btn"]').click()
time.sleep(8)
submit=browser.find_element(By.XPATH,'//*[@id="submit_btn"]').click()
time.sleep(12)