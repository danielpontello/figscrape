from dataclasses import dataclass
from datetime import datetime


@dataclass
class StoreItem:
    name: str = None
    description: str = None
    status: str = None
    price: float = None
    currency: str = None
    store: str = None
    country: str = None
    url: str = None
    scrape_time: datetime = None
    available_date: datetime = None

    def __str__(self):
        return '\n'.join(f'{key}: {value}' for key, value in vars(self).items() if value)
