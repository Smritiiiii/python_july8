import sqlite3
import requests
from bs4 import BeautifulSoup


url = 'https://www.gharghaderi.com/house-for-sale/kathmandu/' 


response = requests.get(url)
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')


conn = sqlite3.connect('houses.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS houses (
        id INTEGER PRIMARY KEY ,
        title TEXT,
        land TEXT,
        road TEXT
    )
''')


items = soup.find_all('div', class_='grid-item')

for item in items:
   
    title = item.find('div', class_='title').text.strip()
    land = item.find('p', class_='land').text.strip()
    road = item.find('p', class_='road').text.strip()
    
   
    cursor.execute('''
        INSERT INTO houses (title, land, road)
        VALUES (?, ?, ?)
    ''', (title, land, road))


conn.commit()
conn.close()

print("Data has been successfully scraped and saved to the SQLite database.")
