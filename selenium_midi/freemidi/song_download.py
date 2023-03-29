from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv

# read csv file

songs_download = []
with open('song_links.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        songs_download.append(row[0])
songs_download.pop(0)
print(len(songs_download))
download_dir = 'D:\Freemidi'

for i in range(len(songs_download)):
    print(f'Download: {i+1}')
    s = Service(executable_path="C:\Development\chromedriver.exe")  # this is the path to your chrome web driver
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=s, options=options)
    params = {'behavior': 'allow', 'downloadPath': download_dir}
    driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)
    driver.get(songs_download[i])
    sleep(1)
    try:
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadmidi"]')))
        download_button.send_keys(Keys.CONTROL + Keys.RETURN)
    except:
        print("Download Failed due to connection.")

    try:
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="aswift_3"]')))
        driver.switch_to.frame(iframe)
        ads = driver.find_element(By.XPATH, '//*[@id="report-button"]')
        actions.move_to_element(ads).move_by_offset(100, 0)
        actions.click().perform()
    except:
        print("No ads.Continue download.")
    sleep(4)
    driver.close()






