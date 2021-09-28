from dataclasses import dataclass
from datetime import datetime


@dataclass
class StoreItem:
    name: str
    description: str
    status: str
    price: float
    currency: str
    store: str
    country: str
    url: str
    scrape_time: datetime
    available_date: datetime
