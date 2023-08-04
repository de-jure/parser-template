"""This module is for getting HTML from page URL."""

import time
import requests


def get_html(url: str) -> str:
    """Get HTML from page URL.

    Args:
        url (str): URL of the page.

    Returns:
        str: HTML of the page.
    """
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text

            print(f'[{response.status_code}]: {url}')
            time.sleep(60)

        except Exception as err: # pylint: disable=broad-except
            print(f'[{err}]: {url}')
            time.sleep(60)
