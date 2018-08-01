from bs4 import BeautifulSoup
import urllib3
import certifi

class WebScrapingService:

    # Constructor
    def __init__(self):
        self.soup = BeautifulSoup('', features="html5lib")

    # Scrape from a URL
    def getFileFromUrl(self, url):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = http.request('GET', url)
        return r.data if r.status == 200 else None

    # Returning the scraped properties
    def get_scraped_properties(self, scrapedResult, type):
        return {
            'title': scrapedResult.title.string
            # TODO: Add more content to be returned
        }[type]

    # Scrape the file
    def scrapeFromFile(self, filePath):
        self.set_soup(BeautifulSoup(open(filePath, 'r'), features="html5lib"))
        if (self.get_soup() != None):
            print("Scraping Completed")
            return self.get_soup()
        else:
            print("Soup Library Error")
            return None

    # Scrape from a URL
    def scrapeFromUrl(self, url):
        data = self.getFileFromUrl(url)
        self.set_soup(BeautifulSoup(data, features="html5lib"))
        if(self.get_soup() != None):
            print("Scraping Completed")
            return self.get_soup()
        else:
            print("Scraping Completed")
            return None


    # Getter for Soup
    def get_soup(self):
        return self.soup

    # Setter for Soup
    def set_soup(self, soup):
        self.soup = soup