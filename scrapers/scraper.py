from abc import ABC, abstractmethod
from typing import List

from .item import StoreItem


class _ScraperInterface(ABC):
    @staticmethod
    @abstractmethod
    def get_short_name() -> str:
        raise NotImplementedError

    @abstractmethod
    def scrape(self, search_term: str) -> List[StoreItem]:
        raise NotImplementedError


class ScraperError(BaseException):
    pass
