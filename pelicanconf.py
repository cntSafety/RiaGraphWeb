from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent
AUTHOR = 'RiaGraph'
SITENAME = 'RiaGraph'
SITEURL = ''
PATH = 'content'
THEME = 'theme'
OUTPUT_PATH = 'dist'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = []
STATIC_PATHS = ['assets']
EXTRA_PATH_METADATA = {
    'assets/style.css': {'path': 'style.css'},
    'assets/riacore.png': {'path': 'riacore.png'},
}
DIRECT_TEMPLATES = []
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
DELETE_OUTPUT_DIRECTORY = True
MARKDOWN = {'extension_configs': {'markdown.extensions.extra': {}}, 'output_format': 'html5'}
with (ROOT / 'content/home.yaml').open(encoding='utf-8') as source:
    LANDING = yaml.safe_load(source)
with (ROOT / 'content/navigation.yaml').open(encoding='utf-8') as source:
    NAVIGATION = yaml.safe_load(source)
TIMEZONE = 'UTC'
FEED_ATOM = None
AUTHOR_FEED_ATOM = None
TAG_FEED_ATOM = None
