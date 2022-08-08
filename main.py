from bs4 import BeautifulSoup
import requests

# requesting information from a website
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                         '=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# for loop to iterate each element
for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    experience_required = job.find('li').text.replace('card_travel', '')
    job_location = job.find('span').text
    skills = job.find('span', class_='srp-skills').text.replace(' ', '')
    print(f'''
    Company Name: {company_name}
    Required Experience: {experience_required}
    Job Location: {job_location}
    Required Skills: {skills}
    ''')



