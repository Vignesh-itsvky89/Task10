import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
paths = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://www.instagram.com/guviofficial/")
time.sleep(5)
driver.maximize_window()
Followers = (driver.find_element(By.XPATH,value= '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span'))
print("Number of Followers:", Followers.text)
Following = (driver.find_element(By.XPATH,value= '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span'))
print("Number of Followings:", Following.text)