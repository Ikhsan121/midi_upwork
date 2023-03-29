'''This script is to download midi in composer filter'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv

start = time.time()
# read csv file composer_links to go to each web page
download_dir = 'D:\Midiworld\ composer'
songs_download = []
with open('composer_links.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        songs_download.append(row[0])
songs_download.pop(0)

# Remove item that is not useful in downloading midi files
for i in range(len(songs_download)):
    if 'search' in songs_download[i]:
        songs_download[i] = ''
    elif 'files' in songs_download[i]:
        songs_download[i] = ''
    elif '.com//' in songs_download[i]:
        songs_download[i] = ''
    elif '.com/#' in songs_download[i]:
        songs_download[i] = ''
    elif 'midifile' in songs_download[i]:
        songs_download[i] = ''
    elif 'index' in songs_download[i]:
        songs_download[i] = ''
    elif 'htm#' in songs_download[i]:
        songs_download[i] = ''

# remove empty items in the list
# create new list using filter function
songs_download = list(filter(lambda x: x not in '', songs_download))

# delete duplicate items
songs_download_remove_duplicated = []
for song in songs_download:
    if song not in songs_download_remove_duplicated:
        songs_download_remove_duplicated.append(song)
print(songs_download_remove_duplicated)
print(len(songs_download_remove_duplicated))

# Go to each download link
for i in range(len(songs_download_remove_duplicated)):
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
        click_download = []
        element = []
        print(f'Go to link number: {i+1}, {songs_download_remove_duplicated[i]}')
        driver.get(songs_download_remove_duplicated[i])
        sleep(2)
        # find all list
        page = driver.find_element(By.ID, 'page')
        hyperlink_midi = page.find_elements(By.TAG_NAME, 'a')
        # store all links in click_download
        for link in hyperlink_midi:
            download = link.get_attribute('href')
            download_element = link
            element.append(download_element) # list of download element
            click_download.append(download) # list of href

        # click all download elements
        print(f'Download page {songs_download_remove_duplicated[i]}')
        for j in range(len(click_download)):
            if 'other' in str(click_download[j]):
                element[j].click()
                print(f'click on {click_download[j]}')
                sleep(1)
            else:
                print('No download link.')

    except:
        print("Failed to download.")

    driver.close()
    end = time.time()
    print(f"Completed in {(end - start) / 60:.2f} minutes")

