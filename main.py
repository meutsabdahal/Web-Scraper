from bs4 import BeautifulSoup
import requests

# requesting information from a website
html_text = requests.get('https://www.upwork.com/nx/jobs/search/?q=python&sort=recency').text
print(html_text)



