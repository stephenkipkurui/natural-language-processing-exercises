from requests import get
from bs4 import BeautifulSoup
import pandas as pd

# def get_blog_articles():
#
#     return ''

def get_people_web_scrap_data():
    
    url = 'https://web-scraping-demo.zgulde.net/people'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    people = soup.select('div.person')
    pple = people[0]

    output = {}

    output['name'] = pple.find('h2').text

    output['quote'], \
    output['email'], \
    output['phone'], \
    output['address'] = [p.text for p in pple.find_all('p')]

    return output

