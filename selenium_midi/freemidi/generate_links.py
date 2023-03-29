from time import sleep
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

start = time.time()
links = []
song_links = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
    , 'w', 'x', 'y', 'z']

for i in range(9):
    zero = "https://freemidi.org/songtitle-0-" + str(i)
    links.append(zero)

for j in range(len(alphabet)):
    for i in range(101):
        zero = f"https://freemidi.org/songtitle-{alphabet[j]}-" + str(i)
        links.append(zero)  # Created link to every page of song title

print(f'Number of page is {len(links)}')

for i in range(len(links)):
    if i % 100 == 0:
        print(f"Scraping for row below {i + 100}")
        sleep(2)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(links[i], headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    song_container = soup.find_all('div', class_='song-list-container')
    for song in song_container:
        song_link = "https://freemidi.org" + song.find('a').get('href')
        if song_link == 'https://freemidi.org/download2---':
            print(f'No song link row {i + 1}')
        else:
            song_links.append(song_link)
    print(f"Scrape row {i + 1}")

print('******************************')
print(f"Number of song link row : {len(song_links)}")
song_dict = {
    'links': song_links
}

# Create data frame
df = pd.DataFrame(song_dict)

# saving the dataframe
df.to_csv('song_links.csv', index=False)
print('CSV file created successfully')
end = time.time()

print(f"Completed in {(end - start) / 60:.2f} minutes")
