from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1] / 'site'
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = set(); self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs: self.links.append(attrs[key])
pages = {}
for f in root.glob('*.html'):
    parser = Parser(); parser.feed(f.read_text(encoding='utf-8-sig')); pages[f] = parser
errors = []
for f, parser in pages.items():
    for link in parser.links:
        u = urlsplit(link)
        if u.scheme or u.netloc: continue
        target = (f.parent / unquote(u.path)).resolve() if u.path else f
        if not target.is_file(): errors.append(f'{f.name}: missing {link}')
        elif u.fragment and (target not in pages or u.fragment not in pages[target].ids): errors.append(f'{f.name}: missing fragment {link}')
if errors: raise SystemExit('\n'.join(errors))
print(f'Validated {len(pages)} pages and their local links.')
