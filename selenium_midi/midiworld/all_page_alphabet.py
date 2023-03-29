from bs4 import BeautifulSoup
import requests
import string
from time import sleep
import time
import pandas as pd

# Generate all links
alphabet = list(string.ascii_uppercase)
alphabet_page = []
for i in range(len(alphabet)):
    url = f"https://www.midiworld.com/files/{alphabet[i]}/all/"
    alphabet_page.append(url)
links = []
# Go to each page
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
start = time.time()
for i in range(len(alphabet_page)):
    pages = []
    response = requests.get(alphabet_page[i], headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # pagination
    listing = soup.find('ul', class_='listing')
    next_page = listing.find_all('a')
    for a in next_page:
        pages.append(a['href'].replace("/0", ""))
    sleep(1)
    # Retrieve title urls
    try:
        for j in range(len(pages)-1):
            # scraping process
            print(f"scraping page number: {1 + j } for {alphabet_page[i]} ")
            response = requests.get(pages[j], headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table')
            midi_urls = table.find_all('a') # find all a tag
            for midi_url in midi_urls:
                url = midi_url['href']
                links.append(url)
    except:
        print("Can't retrieve the title. Keep continue.")
end = time.time()
print(f"Completed in {(end - start)/60:.2f} minutes.")
print(links)
print(len(links))

new_link = []
for b in links:
    if b not in new_link:
        new_link.append(b)

print(f'new_link: {len(new_link)}')
# Create data frame
df = pd.DataFrame(links)
# saving the dataframe
df.to_csv('all_page.csv', index=False)
print('CSV file created successfully')

