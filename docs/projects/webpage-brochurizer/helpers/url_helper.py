
from urllib.parse import urlparse

import requests


def normalize_url(url: str) -> str:
    """Ensure URL has a scheme. If missing, prepend https://"""
    parsed = urlparse(url)
    if not parsed.scheme:  # no http/https given
        url = "https://" + url
    return url

def is_url_valid(url: str) -> bool:
    parsed = urlparse(url)
    is_valid = all([parsed.scheme, parsed.netloc])
    if not is_valid:
        print("Invalid URL. Please enter a valid URL (e.g. example.com)")
        return False
    return True

def is_url_reachable(url: str) -> bool:
    """Check if a URL is reachable (HEAD first, then GET if necessary)."""
    try:
        # Try HEAD request first
        response = requests.head(url, timeout=3, allow_redirects=True)
        if response.status_code >= 400:
            # Some servers reject HEAD, fallback to GET
            response = requests.get(url, timeout=3, stream=True, allow_redirects=True)
        if response.status_code >= 400:
            print("Webpage in the given URL is not reachable. Retry with a different URL.")
            return False
        return True
    except requests.RequestException as e:
        print(f"Error reaching the URL: {e}. Retry with a different URL.")
        return False
