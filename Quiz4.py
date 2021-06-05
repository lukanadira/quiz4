import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

f = open('games.csv', 'w', newline='\n')
f.write('Title,Genre, Price\n')
file_obj = csv.writer(f)
file_obj.writerow(['Title', 'Genre', 'Price'])
h = {'accept-Language': 'en-US'}
ind = 0
while ind < 20:
    url = f'https://store.steampowered.com/category/sports_and_racing/#p={str(ind)}&tab=NewReleases'
    r = requests.get(url, headers=h)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')

    all_games_block = soup.find('div', id='NewReleasesRows')
    all_games = all_games_block.find_all(class_='tab_item')

    for each in all_games:

        title = each.find('div', class_='tab_item_name').text
        genre = each.find('span', class_='top_tag').text
        price = each.find('div', class_='discount_final_price').text
        # print(f'title:{title}')
        # print(f'genre:{genre}')
        # print(f'price:{price}')
        file_obj.writerow([title, genre, price])

    ind += 1
    sleep(randint(15, 25))

print('გილოცავთ თქვენ წარმატებით წამოიღეთ მონაცემები!')

