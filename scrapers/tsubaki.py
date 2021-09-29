import logging
from typing import List

import requests
from bs4 import BeautifulSoup

from .item import StoreItem
from .scraper import _ScraperInterface, ScraperError

BASE_URL = 'https://www.tsubaki.pt/pesquisa?controller=search&s={query}'


class TsubakiScraper(_ScraperInterface):
    def scrape(self, search_term: str) -> List[StoreItem]:
        results_page = self._get_page(url=BASE_URL.format(query=search_term))
        return self._extract_data(page=results_page)

    @staticmethod
    def get_short_name() -> str:
        return 'tsubaki'

    @staticmethod
    def _get_page(url: str) -> str:
        response = requests.get(url, verify=False)  # FIXME: certificate chain is not correctly configured in the site
        response_contents = response.text
        if response.ok:
            return response_contents
        else:
            logging.error(f'HTTP request failed with code {response.status_code}: {response_contents}')
            raise ScraperError(f'HTTP request failed with code {response.status_code}')

    @staticmethod
    def _extract_data(page: str) -> List[StoreItem]:
        items: List[StoreItem] = []
        soup = BeautifulSoup(page, 'html.parser')
        raw_items = soup.find_all('article')
        for raw_item in raw_items:
            title_h2 = raw_item.find('h2', {'class': 'product-title'})
            link_a = title_h2.find('a')
            name = link_a.get_text()
            link = link_a['href']
            price = raw_item.find('span', {'class': 'price'}).get_text()
            item = StoreItem(name=name, price=price, url=link)
            items.append(item)
        return items
