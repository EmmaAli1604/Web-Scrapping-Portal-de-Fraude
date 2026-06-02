# Web-Scrapping-Portal-de-Fraude

## Python web scraping project structure

```text
.
├── pyproject.toml
├── README.md
├── src/
│   └── web_scraper/
│       ├── __init__.py
│       ├── main.py
│       └── scraper.py
└── tests/
    └── test_scraper.py
```

## Quick start

```bash
python -m unittest -q
PYTHONPATH=src python -m web_scraper.main https://example.com --preview-chars 200
```
