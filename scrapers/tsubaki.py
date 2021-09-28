from typing import List

import requests
from bs4 import BeautifulSoup

from scrapers.item import StoreItem
from scrapers.scraper import ScraperInterface

base_url = "https://www.tsubaki.pt/pesquisa?controller=search&s={query}"


class TsubakiScraper(ScraperInterface):
    def scrape(self, search_term: str) -> List[StoreItem]:
        start_page = self.get_page(base_url.format(query=search_term))
        self.extract_data(start_page)

    def get_page(self, url: str) -> str:
        req = requests.get(url, verify=False)
        resp = req.text

        if req.status_code == 200:
            return resp

        return None

    def extract_data(self, page: str) -> List[StoreItem]:
        items = {}

        soup = BeautifulSoup(page, 'html.parser')
        items = soup.find_all('article')

        for item in items:
            title_h2 = item.find('h2', {"class": "product-title"})
            link_a = title_h2.find('a')

            name = link_a.get_text()
            link = link_a['href']

            prices = item.find('span', {"class": "price"}).get_text()

            print(name, "\t", prices, "\t", link)

        return {}