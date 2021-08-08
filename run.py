# import modules
import requests
from bs4 import BeautifulSoup


# Extrct Function to Scrape the website
def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    url = f'https://ie.indeed.com/jobs?q=python&l=dublin&start={page}'
    # pass the url into extract function
    r = requests.get(url, headers)
    content = BeautifulSoup(r.content, 'html.parser')
    # return indeed webiste content
    return content


# filter through indeed using find_all function to find certain tags
def transform(content):
    divs = content.find_all('div', class_='slider_container')
    for item in divs:
        title = item.find('h2').text.strip()
        company = item.find('span', class_='companyName').text.strip()
        try:
            salary = item.find('span', class_='salary-snippet').text.strip()
        except:
            salary = ''
        summary = item.find('div', class_='job-snippet').text.strip()

# Store content into a dictionary and append to a list
        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return


joblist = []
content = extract(0)
transform(content)
print(joblist)

