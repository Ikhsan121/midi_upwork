from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
import time

start = time.time()
URL = "https://bitmidi.com/?page="
links = []
for i in range(1, 7549):  # total number of pages
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(URL+str(i), headers=headers)
        print(f'Scrape {URL+str(i)}')
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('a', class_='pointer no-underline fw4 white underline-hover')
        for title in titles:
            link = 'https://bitmidi.com' + title['href']
            links.append(link)
            print('https://bitmidi.com' + title['href'])
        sleep(2)
    except:
        print("Failed to retrieve.")
print(len(links))

# create dataframe
df = pd.DataFrame(links)

# saving the dataframe
df.to_csv('download_page.csv', index=False)
print('CSV file created successfully')
end = time.time()

print(f"Completed in {(end - start)/60:.2f}  minutes")
