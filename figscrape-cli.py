from argparse import ArgumentParser

from scrapers import scrapers


class InputArgs:
    def __init__(self):
        self._parser = ArgumentParser()
        self._load_arguments()
        parsed_arguments = self._parser.parse_args()

        self.parser: str = parsed_arguments.scraper.lower()
        self.search: str = parsed_arguments.search

    def _load_arguments(self):
        self._parser.add_argument(
            '--scraper',
            choices=[scraper_class.get_short_name() for scraper_class in scrapers],
            required=True
        )
        self._parser.add_argument(
            '--search',
            type=str,
            required=True
        )


def main():
    input_args = InputArgs()
    # TODO: process arguments
    # TODO: select scraper
    # TODO: run scraper
    # TODO: format output


if __name__ == '__main__':
    main()
