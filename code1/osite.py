from datetime import datetime
import datetime
import re
import os
from os import path
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
import pickle as pck
import sys
from kiteconnect import KiteConnect
import pickle as pck
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
import os
import time
geoAllowed = webdriver.FirefoxOptions()
geoAllowed.set_preference('geo.prompt.testing', True)
geoAllowed.add_argument('--headless')
geoAllowed.set_preference('geo.prompt.testing.allow', True)
#geoAllowed.headless = True
#driver = webdriver.Chrome('/usr/bin/chromedriver',options=options)
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',options=geoAllowed)

apikey='*******'
apisecret='*********'
loginurl='https://accounts.zoho.in/signin?servicename=zohopeople&signupurl=https://www.zoho.in/people/signup.html'
driver.get(loginurl)
login_xpath = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/form/div[2]/div[1]/div/span/input')
login_xpath.send_keys('sahil.singh@quantiphi.com')
driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/form/button').click()
c=0
while(c!=3):
    try:
        driver.implicitly_wait(25)
        time.sleep(7)
        password = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/form/div[2]/div[2]/div[2]/input')
        password.send_keys('********')
        c=3
    except Exception as e:
        print(e)
        time.sleep(2)
        c = c+1
print('reached here')
c=0
while(c!=3):
    try:
        driver.implicitly_wait(12)
        signin = '/html/body/div[5]/div[3]/div[2]/form/button'
        driver.find_element_by_xpath(signin).click()
        print('waitign for sign in')
        c=3
    except Exception as e:
        print(e)
        c = c+1
print('after sign in')
driver.implicitly_wait(5)
c=0
try:
 loglimit=driver.find_element_by_xpath('/html/body/div[2]/div/a')
 if (loglimit.is_displayed()):
    loglimit.click()
except Exception as e:
    print(e)
    print('probably not reached login limit yet')


while(c!=3):
    global action
    try:
     driver.implicitly_wait(40) 
     checkin = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div')
     #wait = WebDriverWait(checkin, 20)
     #wait.until(EC.visibility_of_element_located((By.xpath, '/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div'))).click()
     time.sleep(4)
     #checkin.click()
     if(os.getenv('action')=='check-in'):
         if (checkin.text=="Check-in"):
             checkin.click()
         else:
             print("already checked in")
     elif (os.getenv('action')=='check-out'):
         if (checkin.text=="Check-out"):
             checkin.click()
         else:
             print("already checked out")

     time.sleep(3)
     print(checkin.text)
     #driver.implicitly_wait(20) 
     #obj = driver.switch_to.alert
     #obj.accept()
     c=3
    except Exception as e:
     print(e)
     time.sleep(2)
     c = c+1
exit = '/html/body/div[2]/nav/div/div[2]/div[2]/img'
driver.find_element_by_xpath(exit).click()
time.sleep(2)
try:
    signout='/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div/a[2]'
    driver.find_element_by_xpath(signout).click()
    print("signout code seems to have worked")
except Exception as e:
    print(e)
    print("didnt work")


print("seems done")
driver.quit()
