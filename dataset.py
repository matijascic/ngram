import os
import re
from unidecode import unidecode
import re

DATASETS = {
    "en": "./datasets/english/",
    "fr": "./datasets/french/",
    "de": "./datasets/german/",
    "es": "./datasets/spanish/",
    "lat": "./datasets/latin/",
}

def strip_html(text):
    return re.sub(r'<[^>]+>', '', text)

def load_dataset(lang):
    directory = DATASETS[lang]
    if not os.path.isdir(directory):
        print(f"Directory {directory} not found. Run download_datasets.sh first.")
        return {}

    dataset = {}
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if not os.path.isfile(path):
            continue

        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        content = strip_html(content)
        content = unidecode(content)  # converts everything to latin
        content = content.replace('\n', ' ')
        content = ''.join(c for c in content if c.isalpha() or c == ' ')    
        content = re.sub(r' +', ' ', content)  # collapse multiple spaces
        content = content.lower()
        content = " " + content + " "

        dataset[name] = {
            "title": name,
            "path": path,
            "content": content,
        }
        print(f"  Loaded {name} ({len(content)} chars)")

    return dataset