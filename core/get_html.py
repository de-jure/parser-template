import time


import requests


def get_html(URL: str) -> str:
    """Get HTML from page URL

    Args:
        URL (str): URL of page

    Returns:
        str: HTML of page
    """

    while True:
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                return response.text
            else:
                print(f'[{response.status_code}]: {URL}')
                time.sleep(60)
        except Exception as e:
            print(f'[{e}]: {URL}')
            time.sleep(60)
