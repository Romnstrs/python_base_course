import requests
from bs4 import BeautifulSoup
import csv
import time
import sqlite3

header = {
    'User-Agent':
         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
     'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


def get_data(url):
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        # with open('rozetka.html', 'w') as f:
        #     f.write(response.text)
        return response.text
    return None


def parse_data(data):
    soup = BeautifulSoup (data, 'html.parser')
    li_lst = soup.find_all('li', attrs={'class': 'catalog-grid__cell'})
    res = []
    for li in li_lst:
        tmp = {}
        a = li.find('a', attrs={'class': 'goods-tile__heading'})
        href = a['href']
        text = a.text
        old_price = ''
        raw_old = li.find('div', attrs={'class': 'goods-tile__price--old'})
        if raw_old:
            old_price = raw_old.text
            if old_price:
                old_price = int(''.join(i for i in old_price if i.isdigit()))
            else:
                old_price = ''
        raw_price = li.find('div', attrs={'class': 'goods-tile__price'})
        price = raw_price.text
        price = int(''.join(i for i in price if i.isdigit()))
        tmp = {
            'href': href, 'text': text, 'price': price, 'old_price': old_price
        }
        #tmp = (href, text, price, old_price)
        res.append(tmp)
    return res


def save_to_csv(rows):
    csv_title = ['href', 'text', 'price', 'old_price', ]
    with open('videocards.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)


def save_to_db(rows):
    sqlite_connection = sqlite3.connect('cards.db')
    sqlite_create_table_query = '''
        CREATE TABLE IF NOT EXISTS video_cards (
            id INTEGER PRIMARY KEY,
            href TEXT NOT NULL,
            title TEXT NOT NULL,
            price INTEGER NOT NULL,
            old_price INTEGER NULL            
        );'''
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()

    sqlite_connection = sqlite3.connect('cards.db')
    cursor = sqlite_connection.cursor()
    cursor.executemany(
        "INSERT INTO video_cards('href', 'title', 'price', 'old_price' ) VALUES (?,?,?,?)",
        rows)
    sqlite_connection.commit()


def main():
    url = 'https://hard.rozetka.com.ua/videocards/c80087/page={}/'
    res = []
    for i in range(1, 3):
        data = get_data(url.format(i))
        res += parse_data(data)
        time.sleep(2)
    save_to_csv(res)


if __name__ == '__main__':
    main()
