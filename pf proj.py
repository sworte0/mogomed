
url = "https://amdm.ru/akkordi/sektor_gaza/92604/30_let/"
# url = input("введите url")

import requests
response = requests.get(url)
# print(response.status_code)
# print(response)
# print(response.text)

sel = "#body > div.content-table > article > div.b-podbor > div:nth-child(2) > h1 > span:nth-child(1)"

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("meta"))

artist = soup.select_one(sel)

print(artist)
print(artist.text)

sel2 = "#body > div.content-table > article > div.b-video > div > iframe"
print(soup.select_one(sel2).attrs)


input("")
url = f"https://amdm.ru/search/?q="

response = requests.get(url)

vrf = input()
url = f"https://amdm.ru/search/?q={vrf}"
soup = BeautifulSoup(response.text, "html.parser")
sel3 = "#body > div.content-table > article > h1"
res1 = soup.select("meta")
res = soup.select_one(sel3)
print(res1)
print(res)
print(soup.select_one("#body > div.content-table > article > table > tbody > tr:nth-child(1) > td.artist_name"))


