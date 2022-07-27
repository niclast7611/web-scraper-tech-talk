import csv
from datetime import datetime
from turtle import position
from urllib import response
from xml.dom.minidom import Attr
import requests
# BeautifulSoup is python library for pulling data from HTML or XML
from bs4 import BeautifulSoup
import soupsieve

def get_url(position, location):
    # Pick a url to use and look at syntax
    # https://www.indeed.com/jobs?q=full+stack+developer&l=san+diego+ca&jobs.html
    template = 'https://www.indeed.com/q-{}-l-{}-jobs.html'
    url= template.format(position, location)
    return url

def get_record(card):
    # Chrome inspector and pulling specific div names with info you need
    spantag = card.h2.a.span
    hreftag = card.h2.a
    job_title = spantag.get('title')
    job_url = 'https://www.indeed.com' + hreftag.get('href')
    company = card.find('span', 'companyName').text.strip()
    location = card.find('div', 'companyLocation').text.strip()
    snippet = card.find('div', 'job-snippet').text.strip()
    date_posted = card.find('span', 'date').text.strip()
    today = datetime.today().strftime('%Y-%m-%d')
    try:
        salary = card.find('span', 'estimated-salary').text.strip()
    except AttributeError:
        salary='Not Listed'
    record = (job_title, company, location, salary, date_posted, today, snippet, job_url)
    return record

def main(position, location):
    """Run the main program routine"""
    records = []
    url = get_url(position, location)
    
    while True:
        # Begins the request to the website for HTML and looks for the specific job card
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'slider_container')
           
        for card in cards: 
            record = get_record(card)
            records.append(record)
            
        try:
            # Goes through every page of listings until there are no more
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break
    
    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        # Saving the data into a csv file
        writer = csv.writer(f)
        writer.writerow(['Job Title', 'Company', 'Location', 'Salary', 'Date Posted', 'Todays Date', 'Summary', 'URL'])
        writer.writerows(records)

main('full stack developer', 'san diego, ca')
# Runs the function 
