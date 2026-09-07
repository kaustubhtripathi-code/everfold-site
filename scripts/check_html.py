"""Run: python scripts/check_html.py (stdlib only)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

class Check(HTMLParser):
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for value in a.values():
            assert not value or not any(t in value for t in ('<link', '<style', '<meta')), 'HTML tag swallowed by attribute'
        if tag == 'link' and a.get('rel') == 'icon' and 'data:image/svg+xml,' in a.get('href', ''):
            assert '</svg>' in unquote(a['href']), 'Incomplete SVG icon'

root = Path(__file__).resolve().parents[1]
pages = list(root.rglob('*.html'))
assert pages, 'No pages found'
for page in pages:
    try:
        Check().feed(page.read_text(encoding='utf-8-sig'))
    except AssertionError as error:
        raise AssertionError(f'{page.relative_to(root)}: {error}') from error
print(f'PASS: {len(pages)} HTML pages have no swallowed tags or truncated SVG icons')
