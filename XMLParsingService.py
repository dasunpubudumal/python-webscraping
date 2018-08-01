from bs4 import BeautifulSoup

class XMLScrapingService:

    # Constructor
    def __init__(self):
        self.soup = BeautifulSoup('', features="xml")

    # Scrape the file
    def scrapeFromFile(self, filePath):
        self.set_soup(BeautifulSoup(open(filePath, 'r'), features="xml"))
        if (self.get_soup() != None):
            print("Scraping Completed")
            return self.get_soup()
        else:
            print("Soup Library Error")
            return None

    # Getter for Soup
    def get_soup(self):
        return self.soup

    # Setter for Soup
    def set_soup(self, soup):
        self.soup = soup
