"""Core scraping utilities."""

from urllib.request import Request, urlopen


def fetch_html(url: str, timeout: int = 10) -> str:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=timeout) as response:  # nosec B310
        return response.read().decode("utf-8", errors="replace")
