import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from web_scraper.scraper import fetch_html


class _FakeResponse:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return b"<html><title>ok</title></html>"


class FetchHtmlTests(unittest.TestCase):
    @patch("web_scraper.scraper.urlopen", return_value=_FakeResponse())
    def test_fetch_html_returns_decoded_html(self, _mock_urlopen):
        html = fetch_html("https://example.com")
        self.assertIn("<title>ok</title>", html)


if __name__ == "__main__":
    unittest.main()
