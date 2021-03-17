import pandas as pd
import requests
import re
import os
import urllib.request
from bs4 import BeautifulSoup

df = pd.DataFrame()
# url = 'https://w.atwiki.jp/jubeat/pages/1947.html'
# linksource = requests.get(url=url).text
url = 'file:///C:/Users/shzeng/Downloads/git/jubeat_list/wikipage.html'
urlread = urllib.request.urlopen(url).read()
linksource = str(BeautifulSoup(urlread, 'html.parser'))

findit = re.finditer(r'-7--><td style="">(.+)</td>', linksource)
# print(len(re.findall(r'-7--><td style="">(.+)</td>', linksource)))
# print(len(re.findall(r'-9--><td style="">', linksource)))

count = 0
info_dic = {}

for i in findit:
    location = i.start()
    musicinfo = linksource[location-600:location+200]
    start = musicinfo.find('-0--><td style')
    musicinfo = musicinfo[start:]
    end = musicinfo.find('</tr>')
    musicinfo = musicinfo[:end]

    try:
        count += 1
        # title = re.findall(r'title="?\'?(.+) \(\d{,4}d\)', musicinfo)[0]
        title = re.findall(r'title=.{0,2000}\)"?\'?>(.+)</td>', musicinfo)[0]
        title = title.replace('</a>', '').replace('◆', '').replace('&amp;', '&')
        artist = re.findall(r'-1--><td style=".{0,2000}">(.+)</td>', musicinfo)[0]
        artist = artist.replace('&amp;', '&')
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


    except:
        print(musicinfo)
        break

print(count)