import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scraping the website, https://its.taiwanjobs.gov.tw/Course/Detail?ID=153536
def crawl(id):
    print('Crawling course ID:', id)
    url = 'https://its.taiwanjobs.gov.tw/Course/Detail?ID=' + str(id)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get the title of the course in span with class 'col-sm-12'
    title = soup.find('span', class_='col-sm-12').text
    
    # Get the table cell with data-th='上課地點'
    location = soup.find('td', {'data-th': '上課地點'}).text
    
    # Get all content text in the table with class 'RwdTable-unit'
    training_detail = soup.find('table', class_='RwdTable-unit')

    # Get all table rows with class 'td2' under the table 'RwdTable-unit'
    rows = training_detail.find_all('td', class_='td2')
    training_type = rows[0].text
    training_reason = rows[1].text
    training_goal = rows[2].text
    training_expectation = rows[3].text

    # Store the data into a dictionary
    data = {
        'url': url,
        'title': title,
        'location': location,
        'training_type': training_type,
        'training_reason': training_reason,
        'training_goal': training_goal,
        'training_expectation': training_expectation
    }

    # Add the data into a DataFrame
    df = pd.DataFrame([data])

    # Insert the data into a csv file
    df.to_csv('training_courses.csv', mode='a', header=False, index=False)

    print('Data has been successfully crawled and stored in csv file.')


            
if __name__ == '__main__':
    id = 157433
    total_courses_crawled = 0
    while id < 170000:
        try:
            crawl(id)
            id += 1
            total_courses_crawled += 1
        # If the course ID does not exist, skip the course
        except AttributeError:
            id += 1
            continue
    print('Total courses crawled:', total_courses_crawled)

    
