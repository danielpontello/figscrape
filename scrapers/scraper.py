from abc import ABC, abstractmethod
from typing import List

from .item import StoreItem


class ScraperInterface(ABC):
    @abstractmethod
    def scrape(self, search_term: str) -> List[StoreItem]:
        raise NotImplementedError
