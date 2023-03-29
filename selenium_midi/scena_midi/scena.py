from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
URL = "http://www.scena.org/midi/music/"

s = Service(executable_path="C:\Development\chromedriver.exe")  # this is the path to your chrome web driver
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
prefs = {"download.default_directory": 'D:\scena'} # This is the path to your download folder
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=s, options=options)
driver.get(URL)
sleep(2)

table = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[1]/div/table')
rows = table.find_elements(By.XPATH, '//tbody/tr')

links = []
for row in rows:
    try:
        a = row.find_element(By.TAG_NAME, 'a').get_attribute('href')
        if ".mid" in a:
            links.append(a)
        elif ".zip" in a:
            links.append(a)
    except:
        print("The link is not midi file")


for link in links:
    driver.get(link)
    sleep(1)




