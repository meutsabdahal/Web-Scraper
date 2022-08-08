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
    more_info = job.header.h2.a['href']
    print(f'Company Name: {company_name.strip()}')
    print(f'Required Experience: {experience_required}')
    print(f'Job Location: {job_location}')
    print(f'Required Skills: {skills.strip( )}')
    print(f'More Info: {more_info}')
    print('')




