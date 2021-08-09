# import modules
import requests
from bs4 import BeautifulSoup
import pandas as pd

joblist = []


# Extrct Function to Scrape the website
def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
    url = f'https://ie.indeed.com/jobs?q={job_type}&l={location}&start={page}'
    # pass the url into extract function
    r = requests.get(url, headers)
    if not r.status_code == 200:
        raise Exception('No content returning from from url.')
    content = BeautifulSoup(r.content, 'html.parser')
    # return indeed webiste content
    return content


# filter through indeed using find_all function to find certain tags
def transform(content):
    """The transform function is used to
    find specific tags within the html parsed."""
    divs = content.find_all('div', class_='slider_container')
    for item in divs:
        title = item.find('h2').text.strip()
        company = item.find('span', class_='companyName').text.strip()
        try:
            salary = item.find('span', class_='salary-snippet').text.strip()
        except Exception as ex:
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
    return None


if __name__ == '__main__':
    print('what job are you looking for?')
    job_type = input('')

    print('What location are you looking for?')
    location = input('')


# For loop to loop through the first three pages in a step of ten
for i in range(0, 40, 10):
    print(f'Getting page {i} ')
    content = extract(0)
    transform(content)

# Panda dataframe sends the scraped data to the jobs csv file
df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
