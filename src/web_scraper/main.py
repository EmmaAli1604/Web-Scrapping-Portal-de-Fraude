"""CLI entrypoint for running a basic scrape."""

import argparse

from web_scraper.scraper import fetch_html


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch HTML content from a URL")
    parser.add_argument("url", help="Target URL to scrape")
    parser.add_argument("--preview-chars", type=int, default=500, help="Characters to print")
    args = parser.parse_args()

    html = fetch_html(args.url)
    print(html[: args.preview_chars])


if __name__ == "__main__":
    main()
