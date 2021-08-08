import requests
from bs4 import BeautifulSoup


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    url = f'https://ie.indeed.com/jobs?q=python&l=dublin&start={page}'
    r = requests.get(url, headers)
    return r.status_code

print(extract(0))
