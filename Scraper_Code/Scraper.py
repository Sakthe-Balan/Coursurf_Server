import requests
from bs4 import BeautifulSoup
import csv
import time
from requests.exceptions import RequestException, ChunkedEncodingError
from urllib3.exceptions import ProtocolError
import re

filename = 'Course_Info(Final)1.csv'
fields = ['title','type', 'Provider', 'taught_by', 'Link', 'url', 'side_card', 'overview', 'ratings', 'no_of_ratings']

with open(filename, 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
c=int(input("enter the initial page to start from: "))
a=int(input("enter number of pages to be scraped : "))
b=input("enter teh link query to extract EX:/provider/udemy: ")
for i in range(c,c+a):
    # Define the URL of the webpage containing the links to be scraped
    url = 'https://www.classcentral.com'+b+'?page=' + str(i)

    # Define the headers to be used for making requests to the website
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close",
        "Upgrade-Insecure-Requests": "1"}

    # Send a GET request to the website and parse the HTML content using BeautifulSoup
    while True:
        try:
            page = requests.get(url, headers=headers)
            break
        except (RequestException, ProtocolError) as e:
            print(f"Error: {e}")
            time.sleep(2)  # wait for 2 seconds before retrying
            continue

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    # Loop through all the links in the webpage and scrape the data inside each of them
    for link in soup2.find_all('a', attrs={'class': 'color-charcoal course-name'}):
        link_url = link['href']
        link_url = 'https://www.classcentral.com' + link_url
        print(link_url, i)
        if link_url == 'https://www.classcentral.com/course/udemy-copywriter-32281 121':
            continue

        # Send a GET request to the link and parse the HTML content using BeautifulSoup
        retry_count = 0
        while retry_count < 3:
            try:
                link_page = requests.get(link_url, headers=headers)
                link_soup1 = BeautifulSoup(link_page.content, 'html.parser')
                link_soup2 = BeautifulSoup(link_soup1.prettify(), 'html.parser')
                time.sleep(3)

                # Scrape the data inside the link using BeautifulSoup
                try:
                    title = link_soup2.find('h1', attrs={'class': 'medium-up-head-1'}).get_text().strip()
                except AttributeError:
                    print("Title not available. Leaving it blank and continuing...")
                    title = ''
                    continue

                try:
                    type = link_soup2.find('div', attrs={'class': 'small-down-margin-top-small margin-bottom-xsmall medium-up-margin-bottom-small'}).get_text().strip()
                    type = '/'.join(type.split())
                except AttributeError:
                    print("Type not available. Leaving it blank and continuing...")
                    type = ''
                    continue
                dummy=0
                try:
                    ratings = link_soup2.find('p', attrs={'class': 'text-2 medium-down-margin-top-xsmall large-up-margin-left-xsmall inline-block'}).get_text().strip()
                    ratings = ratings.replace('\n', ' ').replace('\r', '')  # Replace line breaks with spaces
                    ratings = re.sub(' +', ' ', ratings)  # Replace multiple spaces with a single space
                except AttributeError:
                    try:
                        p_element = link_soup2.find('p', class_='text-1 medium-down-margin-top-xsmall large-up-margin-left-xsmall inline-block')
                        strong_elements = []
                        if p_element:
                            strong_elements = p_element.find_all('strong', class_='weight-bold')

                        # Extract the text content from the first two <strong> elements
                        rating = strong_elements[0].get_text() if len(strong_elements) > 0 else ''
                        rating= ' '.join(rating.split())
                        number_of_ratings = strong_elements[1].get_text() if len(strong_elements) > 1 else ''
                        number_of_ratings= '/'.join(number_of_ratings.split())
                        dummy=1

                       
                    except AttributeError:
                        print("Ratings not available. Leaving it blank and continuing...")
                        rating = ''
                        number_of_ratings=''
                        continue
                
                if(dummy==0):
                    # Extract the rating and number of ratings using regular expressions
                    rating_match = re.search(r'(\d+(\.\d+)?) rating', ratings)
                    number_of_ratings_match = re.search(r'based on (\d+) ratings', ratings)

                    # Assign the extracted values to separate variables
                    rating = float(rating_match.group(1)) if rating_match else ''
                    number_of_ratings = int(number_of_ratings_match.group(1)) if number_of_ratings_match else ''


                try:
                    provider = link_soup2.find('a', attrs={'class': 'text-1 link-gray-underline'}).get_text().strip()
                except AttributeError:
                    print("Provider not available. Leaving it blank and continuing...")
                    provider = ''
                    continue
                try:
                    h3_with_class = link_soup2.find('div', class_='course-noncollapsable-section')
                    p_with_class = h3_with_class.find('p', class_='text-1')
                    taught_by = p_with_class.get_text().strip()
                except AttributeError:
                    print("Taught by not available. Leaving it blank and continuing...")
                    taught_by = ''

                try:
                    link = link_soup2.find('a', attrs={'class': 'btn-blue btn-medium width-100 padding-horz-xlarge'}).get('href').strip()
                    link = 'https://www.classcentral.com' + link
                except AttributeError:
                    print("Link not available. Leaving it blank and continuing...")
                    link = ''

                try:
                    a_element = link_soup2.find('a', class_='text-1 link-gray-underline')
                    if(a_element != None):
                        url = a_element['href']
                except AttributeError:
                    print("URL not available. Leaving it blank and continuing...")
                    url = 'b'

                try:
                    li_list = link_soup2.find_all('li', class_='course-details-item border-gray-light')
                    side_cards = []

                    for li_with_class in li_list:
                        span_with_class = li_with_class.find('span', class_='text-2 line-tight')
                        if span_with_class:
                            side_card = span_with_class.get_text().strip()
                            # Limit the maximum number of gaps between words to 1
                            side_card = ' '.join(side_card.split())
                            side_cards.append(side_card)
                        else:
                            a_with_class = li_with_class.find('a', class_='text-2 color-charcoal line-tight')
                            if a_with_class:
                                side_card = a_with_class.get_text().strip()
                                # Limit the maximum number of gaps between words to 1
                                side_card = ' '.join(side_card.split())
                                side_cards.append(side_card)

                except AttributeError:
                    print("Side card not available. Leaving it blank and continuing...")
                    side_cards = []

                try:
                    content_element = link_soup2.find('div', class_='truncatable-area')
                    if content_element is None:
                        content_element = link_soup2.find('div', class_='wysiwyg text-1 line-wide')

                    # Extract the raw HTML content from the element
                    if content_element:
                        overview = content_element.prettify()
                    else:
                        overview = ''

                except AttributeError:
                    print("Overview not available. Leaving it blank and continuing...")
                    overview = ''



                

                # Write the scraped data to the CSV file
                with open(filename, 'a', newline='', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow([title,type, provider, taught_by, link, url, side_cards, overview, rating, number_of_ratings])

                break
            except (RequestException, ChunkedEncodingError, ProtocolError) as e:
                print(f"Error: {e}")
                retry_count += 1
                print(f"Retrying... Retry count: {retry_count}")
                time.sleep(2)  # wait for 2 seconds before retrying
                continue
        else:
            print("Failed to retrieve data for the link. Moving on to the next link...")
