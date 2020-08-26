
import json, requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

URL = 'https://www.mcc-mnc.com/'

def scrape_mccs():

    page = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')

    data = {}
    with open('mccs.json', 'w') as json_file:
        for row in soup.find('tbody'):
            if row == '\n':
                continue
            row_items = [item.text for item in row]

            if row_items[0] not in data:
                data[str(row_items[0])] = {}
                data[str(row_items[0])]['iso'] = row_items[2]
                data[str(row_items[0])]['country'] = row_items[3]
                data[str(row_items[0])]['country code'] = row_items[4]
                data[str(row_items[0])]['networks'] = []
            line = {}
            line['mnc'] = row_items[1]
            line['network'] = row_items[5]
            data[str(row_items[0])]['networks'].append(line)

        json.dump(data, json_file)

if __name__ == '__main__':

    scrape_mccs()
