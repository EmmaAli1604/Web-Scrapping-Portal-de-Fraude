import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from web_scraper.scraper import fetch_html


class MockResponse:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return b"<html><title>ok</title></html>"


class FetchHtmlTests(unittest.TestCase):
    @patch("web_scraper.scraper.urlopen", return_value=MockResponse())
    def test_fetch_html_returns_decoded_html(self, _mock_urlopen):
        html = fetch_html("https://example.com")
        self.assertIn("<title>ok</title>", html)

    @patch("web_scraper.scraper.urlopen", return_value=MockResponse())
    def test_fetch_html_passes_timeout_to_urlopen(self, mock_urlopen):
        fetch_html("https://example.com", timeout=3)
        self.assertEqual(mock_urlopen.call_args.kwargs["timeout"], 3)


if __name__ == "__main__":
    unittest.main()
