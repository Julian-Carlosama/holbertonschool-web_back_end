#!/usr/bin/env python3
""" Expiring web cache and tracker
    obtain the HTML content of a particular URL and"""
import redis
import requests
r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """  """
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text
