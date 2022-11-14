import time
from bs4 import BeautifulSoup
import requests


# function to gather data from website and to store the data
def find_jobs():
    # requesting information from a website
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                             '=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # for loop to iterate each element
    for index, job in enumerate(jobs):
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        experience_required = job.find('li').text.replace('card_travel', '')
        job_location = job.find('span').text
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']

        # storing data in a file
        with open(f'files/ {index}.txt', 'w') as f:
            f.write(f'Company Name: {company_name.strip()} \n')
            f.write(f'Required Experience: {experience_required} \n')
            f.write(f'Job Location: {job_location} \n')
            f.write(f'Required Skills: {skills.strip( )} \n')
            f.write(f'More Info: {more_info} \n')
        print(f'File Saved as {index}.txt')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes..')
        time.sleep(time_wait * 60)




