import requests
from bs4 import BeautifulSoup


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    url = f'https://ie.indeed.com/jobs?q=python&l=dublin&start={page}'
    r = requests.get(url, headers)
    content = BeautifulSoup(r.content, 'html.parser')
    return content


def transform(content):
    divs = content.find_all('div', class_='slider_container')
    for item in divs:
        title = item.find('h2').text.strip()
        company = item.find('span', class_='companyName').text.strip()
        try:
            salary = item.find('span', class_='salary-snippet').text.strip()
        except:
            salary = ''
        print(salary)
    return


content = extract(0)
transform(content)


