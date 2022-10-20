from unittest.loader import VALID_MODULE_NAME
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv = Service(executable_path="C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win32\\101.0.4951.41\\chromedriver.exe")
a = webdriver.Chrome(service=serv)

time.sleep(1)
a.get("https://www.instagram.com/")

time.sleep(1)
username = a.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
username.send_keys('Sample_Username')

time.sleep(1)
password = a.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
password.send_keys('XYZ$$$')

# time.sleep(1)
# show =a.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/div/div/button')
# show.click()


# time.sleep(1)
# show =a.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/div/div/button')
# show.click()


time.sleep(1)
send = a.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
send.click()
a.maximize_window()