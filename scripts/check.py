from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1] / 'dist'

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

pages = {}
for file in root.glob('*.html'):
    parser = Parser()
    parser.feed(file.read_text(encoding='utf-8-sig'))
    pages[file] = parser

expected = {'index.html', 'docs.html', 'cheatsheet.html'}
missing = expected - {file.name for file in pages}
errors = [f'Missing generated page: {name}' for name in sorted(missing)]
for file, parser in pages.items():
    for link in parser.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (file.parent / unquote(url.path)).resolve() if url.path else file
        if not target.is_file():
            errors.append(f'{file.name}: missing {link}')
        elif url.fragment and (target not in pages or url.fragment not in pages[target].ids):
            errors.append(f'{file.name}: missing fragment {link}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Validated {len(pages)} pages and their local links.')
