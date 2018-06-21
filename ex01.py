from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen("https://nfljapan.com/season_type/pre_w4/2018")
bsObj = BeautifulSoup(html, 'lxml')
for link in bsObj.find("div", {"id":"content"}).findAll("a", href=re.compile("https://nfljapan.com/score/\w")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
