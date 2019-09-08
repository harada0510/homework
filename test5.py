#日経新聞の日付け,大見出し,日経平均,ダウNY平均を抽出し,カンマ区切りのCSVファイルに出力するスクレイピングプログラム

import requests
import json
from bs4 import BeautifulSoup

r = requests.get('https://www.nikkei.com')

text = r.text

date = text.split('<div class="l-miH02_date">')[1].split('</div>')[0]
title = text.split('<span class="m-miM07_titleL">')[1].split('</span>')[0]
nikkei = text.split('<span class="m-miH01C_rate">')[1].split('</span>')[0].replace(',','')
dau = text.split('<span class="m-miH01C_rate">')[2].split('</span>')[0].replace(',','')

a = open("nikkei.csv","w")

a.write('日付,大見出し,日経平均,NYダウ')
a.write(date + ',' + title + ',' + nikkei + ',' + dau + '\n')

a.close()
