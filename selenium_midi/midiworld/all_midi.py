"""Sometimes the file doesn't exist. This will make a new tab open and not close by the webdriver. So you can
 close the window manually."""
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

page_title = []
# read csv file
with open('all_page.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        page_title.append(row[0])
page_title.pop(0) # delete first row

# directory for downloaded midi
download_dir = 'D:\Midiworld\ all'
# go to each page
for i in range(len(page_title)-1630):
    # Set up the chrome web driver
    s = Service(executable_path="C:\Development\chromedriver.exe")  # this is the path to your chrome web driver
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
    prefs = {"download.default_directory": download_dir}  # This is the path to your download folder
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(page_title[i])
        print(page_title[i])
        sleep(1)
        links = driver.find_elements(By.TAG_NAME, 'ul')[1]
        urls = links.find_elements(By.TAG_NAME, 'a')
        for url in urls:
            url.click()
            sleep(2)
    except:
        print("Failed to download. Keep continue")
    sleep(1)
    driver.close()



