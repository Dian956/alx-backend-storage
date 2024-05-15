import requests
from functools import lru_cache
from time import sleep, time

url_access_count = {}

@lru_cache(maxsize=None)
def get_page(url: str) -> str:
    global url
