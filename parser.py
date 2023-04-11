import pandas as pd
import requests
from bs4 import BeautifulSoup
import json


def parse_it(url, append=False):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table_rows = soup.find_all('tr')

    info_list = []
    for row in table_rows:
        try:
            cells = row.find_all('td')
            if len(cells) > 1:
                title = cells[0].text.strip()
                title = title[:-1] if title[-1] == '◆' else title
                title = title[:-4] + title[-3:] if title[-3:] == '[2]' else title
                artist = cells[1].text.strip()
                bpm = cells[2].text.strip()
                bsc_level = cells[3].text.strip()
                adv_level = cells[4].text.strip()
                ext_level = cells[5].text.strip()
                bsc_note = cells[6].text.strip()
                adv_note = cells[7].text.strip()
                ext_note = cells[8].text.strip()
                info_dict = {'title': title, 'artist': artist, 'bpm': bpm, 'bsc_level': bsc_level,
                             'adv_level': adv_level,
                             'ext_level': ext_level, 'bsc_note': bsc_note, 'adv_note': adv_note, 'ext_note': ext_note}
                info_list.append(info_dict)
        except:
            print(cells)
            break

    if append is False:
        with open('jubeat_list.json', 'w', encoding='utf-8') as js:
            json.dump(info_list, js, ensure_ascii=False)
        pd.DataFrame(info_list).to_csv("jubeat_list.csv", index=False, encoding='utf_8_sig', quoting=1)
    else:
        with open('jubeat_list.json', 'a', encoding='utf-8') as js:
            json.dump(info_list, js, ensure_ascii=False)
        pd.DataFrame(info_list).to_csv("jubeat_list.csv", index=False, encoding='utf_8_sig', quoting=1, mode='a')
