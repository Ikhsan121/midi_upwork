from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

download_dir = 'D:\ johnwilliams'

# set up the chrome webdriver
s = Service(executable_path="C:\Development\chromedriver.exe")  # this is the path to your chrome web driver
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
prefs = {"download.default_directory": download_dir}  # This is the path to your download folder
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=s, options=options)
driver.get('http://johnwilliams.free.fr/midi.php?critere=film')
download_items = driver.find_elements(By.TAG_NAME, 'a')
midi = []
links = []
# store all web elements of midi links
for download in download_items:
    if 'midi/' in download.get_attribute('href'):
        midi.append(download)
        links.append(download.get_attribute('href'))

print(links)
for i in range(len(midi)):
    print(f"click on midi: {i+1}")
    try:
        midi[i].send_keys(Keys.CONTROL + Keys.RETURN)
    except:
        print('Failed to download')

