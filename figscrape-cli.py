import logging
import os
from argparse import ArgumentParser
from typing import List

from pendulum import now

from scrapers import scrapers, StoreItem


class InputArgs:
    def __init__(self):
        self._parser = ArgumentParser()
        self._load_arguments()
        parsed_arguments = self._parser.parse_args()

        self.scraper: str = parsed_arguments.scraper.lower()
        self.search: str = parsed_arguments.search

    def _load_arguments(self):
        self._parser.add_argument(
            '--scraper',
            choices=list(scrapers.keys()),
            required=True
        )
        self._parser.add_argument(
            '--search',
            type=str,
            required=True
        )


def main():
    _configure_logging()
    input_args = InputArgs()
    logging.info(f'Searching "{input_args.scraper}" for "{input_args.search}"...')
    scraper = scrapers[input_args.scraper]()
    store_items = scraper.scrape(search_term=input_args.search)
    _persist(input_args=input_args, store_items=store_items)
    logging.info('Done!')


def _persist(input_args: InputArgs, store_items: List[StoreItem]):
    logging.info('Storing results...')
    if not os.path.exists('./results'):
        os.mkdir('./results')
    with open(f'./results/figscrape-{input_args.scraper}-{input_args.search}-{now().timestamp()}.txt',
              'w', encoding='utf-8') as file:
        file.writelines([str(item) + '\n\n' for item in store_items])


def _configure_logging():
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger('urllib3').setLevel(logging.CRITICAL)


if __name__ == '__main__':
    main()
