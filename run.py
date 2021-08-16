# import modules
import requests
from bs4 import BeautifulSoup
from beautifultable import BeautifulTable

joblist = []


# Extract Function to Scrape the website
def extract(page, job_type, location):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }
    url = f"https://ie.indeed.com/jobs?q={job_type}&l={location}&start={page}"
    # pass the url into extract function
    r = requests.get(url, headers)
    if not r.status_code == 200:
        raise Exception("No content returning from from url.")
    content = BeautifulSoup(r.content, "html.parser")
    # return indeed website content
    return content


# filter through indeed using find_all function to find certain tags
def transform(content):
    """The transform function is used to
    find specific tags within the html parsed."""
    divs = content.find_all("div", class_="slider_container")
    for item in divs:
        title = item.find("h2").text.strip()
        company = item.find("span", class_="companyName").text.strip()
        try:
            salary = item.find("span", class_="salary-snippet").text.strip()
        except Exception as ex:
            salary = "Salary not available"
        summary = item.find("div", class_="job-snippet").text.strip()

        # Store content into a dictionary and append to a list
        job = {
            "title": title,
            "company": company,
            "salary": salary,
            "summary": summary
        }
        joblist.append(job)
    return None


# User inputs to find specific Jobs and locations
if __name__ == "__main__":
    print("What job are you looking for?")
    print("Note: You may look for standard job types such as developer, chef, recruiter, etc.")
    job_type = ""
    while not job_type:
        job_type = input("")
        if not job_type:
            print("Please provide some input.")
    print("")

    print("Where are you looking to work?")
    print("Note: You will only get results if the location is within Ireland")
    location = ""
    while not location:
        location = input("")
        if not location:
            print("Please provide some input.")
    print("")


# For loop to loop through the first three pages in a step of ten
    for i in range(0, 40, 10):
        print(f"Getting page {i} ")
        content = extract(i, job_type, location)
        transform(content)

    print("")
    print("You searched for {} jobs in {}".format(
        job_type,
        location
    ))
    if len(joblist) == 0:
        print("Sorry, no jobs found!")
    else:
        print(joblist)

        print("")
        print("Summary:")
        # initialise pretty table
        table = BeautifulTable()
        for job in joblist:
            # Insert table rows
            table.rows.append([
                job.get("title"),
                job.get("company"),
                job.get("salary")
            ])

        table.columns.header = ["Title", "Company", "Salary"]
        print(table)

        # print("")
        # print("See above for full iterable list!")

    # print("")
    # print("Thanks for using my application to find your next job!")
