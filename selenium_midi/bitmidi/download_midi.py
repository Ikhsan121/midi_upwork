import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
download_page = []
# read csv file
with open('download_page.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        download_page.append(row[0])
download_page.pop(0) # delete first row
print(len(download_page))
# directory for downloaded midi
download_dir = 'D:\ bitmidi'
# open page
for i in range(len(download_page)):
    print(f"Download number: {i + 1}")
    # set up the chrome webdriver
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
    driver.get(download_page[i])
    try:
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[1]/div[4]/div[2]/p/a')))
        download_button.send_keys(Keys.CONTROL + Keys.RETURN)
    except:
        print("Download failed due to connection.")
    try:
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="aswift_4"]')))
        driver.switch_to.frame(iframe)
        ads = driver.find_element(By.XPATH, '//*[@id="report-button"]')
        actions.move_to_element(ads).move_by_offset(100, 0)
        actions.click().perform()
    except:
        print("No ads.Continue download.")
    sleep(4)
    driver.close()
