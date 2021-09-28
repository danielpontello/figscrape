from typing import Type, Dict

from .item import StoreItem
from .scraper import _ScraperInterface
from .tsubaki import TsubakiScraper

scrapers: Dict[str, Type[_ScraperInterface]] = {TsubakiScraper.get_short_name(): TsubakiScraper}
