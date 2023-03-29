import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
URL = 'https://www.midiworld.com/composers.htm'
# Scraping process
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

all_links = []
hrefs = soup.find_all(href=True)  # Retrieve all links from web page
for href in hrefs:
    url = 'https://www.midiworld.com/' + href['href']
    all_links.append(url)

# Create data frame
df = pd.DataFrame(all_links)

# saving the dataframe
df.to_csv('composer_links.csv', index=False)
print('CSV file created successfully')


