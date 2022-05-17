import pandas as pd
import re
import os
import urllib.request
from bs4 import BeautifulSoup
import json


def parse_it(url):
    urlread = urllib.request.urlopen(url).read()
    linksource = str(BeautifulSoup(urlread, 'html.parser'))

    findit = re.finditer(r'-7--><td style="">(.+)</td>', linksource)  # 用adv_note定位源代码中每首曲子的位置
    # print(len(re.findall(r'-7--><td style="">(.+)</td>', linksource)))

    info_list = []
    for i in findit:
        location = i.start()
        musicinfo = linksource[location - 600:location + 200]  # 包含全部谱面信息
        start = musicinfo.find('-0--><td style')
        musicinfo = musicinfo[start:]
        end = musicinfo.find('</tr>')
        musicinfo = musicinfo[:end]  # 筛选从标题到ext_note的信息

        try:
            title = re.findall(r'title=.{0,2000}\)"?\'?>(.+)</td>', musicinfo)[0]
            title = title.replace('</a>', '').replace('◆', '').replace('&amp;', '&')
            artist = re.findall(r'-1--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
            artist = artist.replace('&amp;', '&').replace('<br/>', '')
            bpm = re.findall(r'-2--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
            bsc_level = re.findall(r'-3--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
            bsc_level = bsc_level if len(bsc_level) < 5 else bsc_level[3:-4]
            adv_level = re.findall(r'-4--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
            adv_level = adv_level if len(adv_level) < 5 else adv_level[3:-4]
            ext_level = re.findall(r'-5--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
            ext_level = ext_level if len(ext_level) < 5 else ext_level[3:-4]
            bsc_note = re.findall(r'-6--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
            adv_note = re.findall(r'-7--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
            ext_note = re.findall(r'-8--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
            info_dict = {'title': title, 'artist': artist, 'bpm': bpm, 'bsc_level': bsc_level, 'adv_level': adv_level,
                         'ext_level': ext_level, 'bsc_note': bsc_note, 'adv_note': adv_note, 'ext_note': ext_note}
            info_list.append(info_dict)
        except:
            print(musicinfo)
            break

    with open('jubeat_list.json', 'w', encoding='utf-8') as js:
        json.dump(info_list, js, ensure_ascii=False)
    pd.DataFrame(info_list).to_csv("jubeat_list.csv", index=False, encoding='utf_8_sig', quoting=1)


if __name__ == "__main__":
    url = 'https://w.atwiki.jp/jubeat/pages/1947.html'
    # url = 'file:///' + os.path.abspath('.') + '/wikipage.html'
    parse_it(url)
