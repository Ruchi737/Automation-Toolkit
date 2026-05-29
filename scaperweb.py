import requests
from bs4 import BeautifulSoup

def scrape_website(url):

    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        print("\nPage Titles and Headings:\n")

        headings = soup.find_all("h1")

        for heading in headings:
            print(heading.text.strip())

    except Exception as e:
        print("Error:", e)
