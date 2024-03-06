import requests
from bs4 import BeautifulSoup


miReq = requests.get("https://ac.windtre.it/")

print(miReq.status_code)

print(miReq.headers)

print(miReq.text)