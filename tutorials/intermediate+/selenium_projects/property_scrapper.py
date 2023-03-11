import requests
from bs4 import BeautifulSoup

PROPERTY_LINK = "https://www.zillow.com/detroit-mi/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A42.454445697067875%2C%22east%22%3A-82.89836118896486%2C%22south%22%3A42.25096291641302%2C%22west%22%3A-83.30004881103517%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A17762%2C%22regionType%22%3A6%7D%5D%7D"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

class GetProperties:
    def __init__(self):
        self.response = requests.get(PROPERTY_LINK, headers=HEADERS)
        amazon_response = self.response.text
        self.soup = BeautifulSoup(amazon_response, "lxml")

    
    def get_pagination_count(self):
        return int(self.soup.find(class_="Text-c11n-8-85-1__sc-aiai24-0 bEkett").getText().split()[-1])
    
    def get_all_properties(self):
        # page_count = self.get_pagination_count()
        
        all_listings = self.soup.find( class_="List-c11n-8-85-1__sc-1smrmqp-0 srp__sc-1ieen0c-0 JFapv photo-cards with_constellation")
        print(len(all_listings))
        for list in all_listings:
            print(list.getText())


property = GetProperties()
# print(property.get_pagination_count())
property.get_all_properties()