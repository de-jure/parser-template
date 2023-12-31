"""This module is for getting HTML from page URL."""

import time
import requests


def get_html(url: str, timeout: int = 10) -> str:
    """Get HTML from page URL.

    Args:
        url (str): URL of the page.
        timeout (int, optional): Timeout for the request in seconds. Defaults to 10.

    Returns:
        str: HTML of the page.
    """
    while True:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                return response.text

            print(f'[{response.status_code}]: {url}')
            time.sleep(60)

        except Exception as err:  # pylint: disable=broad-except
            print(f'[{err}]: {url}')
            time.sleep(60)
