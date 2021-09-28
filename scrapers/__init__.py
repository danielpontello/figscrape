from typing import List, Type

from .item import StoreItem
from .scraper import _ScraperInterface
from .tsubaki import TsubakiScraper

scrapers: List[Type[_ScraperInterface]] = [TsubakiScraper]
