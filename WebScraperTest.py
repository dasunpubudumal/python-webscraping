from WebScrapingService import WebScrapingService

if __name__ == '__main__':
    webScrapingService = WebScrapingService()
    scrapingResultFromURL = webScrapingService.scrapeFromUrl("https://www.google.lk")
    print(webScrapingService.get_scraped_properties(scrapingResultFromURL, 'title'))