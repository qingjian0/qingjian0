#!/usr/bin/env python3
import json, random
from pathlib import Path
from datetime import datetime
LEFT = '\u300c'
RIGHT = '\u300d'
DASH = '\u2014\u2014 '
REPO_DIR = Path(__file__).resolve().parent.parent
QUOTES_FILE = REPO_DIR / 'scripts' / 'quotes.json'
README_FILE = REPO_DIR / 'README.md'
with open(QUOTES_FILE, 'r', encoding='utf-8') as f:
    quotes = json.load(f)
random.seed(datetime.now().timetuple().tm_yday)
q = random.choice(quotes)
with open(README_FILE, 'r', encoding='utf-8') as f:
    content = f.read()
marker = '> **' + LEFT
start = content.find(marker)
if start >= 0:
    end = content.find(RIGHT + '**', start)
    if end > start:
        content = content[:start] + marker + q['q'] + RIGHT + '**' + content[end + 4:]
        src_marker = '> *' + DASH
        src_start = content.find(src_marker)
        if src_start >= 0:
            src_end = content.find('*', src_start + 6)
            if src_end > src_start:
                content = content[:src_start] + '> *' + DASH + q['s'] + '*' + content[src_end + 1:]
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated: ' + q['q'])
else:
    print('ERROR: marker not found')
    exit(1)
