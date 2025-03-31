import csv
import random
import string
import requests
from pathlib import Path

WORD_LIST_URL = 'https://hackrange.org/scripts/dictionary.txt'
NAMES_FILE_URL = 'https://hackrange.org/scripts/names.txt'
WORD_LIST_PATH = Path('./dictionary.txt')
NAMES_FILE_PATH = Path('./names.txt')
RESULTS_CSV_PATH = Path('./results.csv')
DOMAIN = 'hackrange.com'
NUM_USERS = 1574

def download_file(url: str, path: Path):
    if not path.exists():
        response = requests.get(url)
        response.raise_for_status()
        path.write_text(response.text)
        print(f'Downloaded {path.name} from {url}')
    else:
        print(f'{path.name} already exists.')

download_file(WORD_LIST_URL, WORD_LIST_PATH)
download_file(NAMES_FILE_URL, NAMES_FILE_PATH)

with WORD_LIST_PATH.open('r') as f:
    WORD_LIST = [
        w.strip().capitalize() for w in f
        if w.strip().isalpha() and len(w.strip()) >= 3
    ]

with NAMES_FILE_PATH.open('r') as f:
    raw_names = [line.strip() for line in f if line.strip()]

def generate_samaccountname(first: str, last: str) -> str:
    base = f"{first[0]}{last}".lower()
    return f"{base}{random.randint(100,999)}"

def generate_password(words: list[str], count: int = 3) -> str:
    chosen = '-'.join(random.sample(words, count))
    return f"{chosen}{random.randint(0,9)}"

def generate_users(names: list[str], limit: int) -> list[dict]:
    users = []
    seen_upns = set()

    for line in names:
        try:
            first, last = [part.capitalize() for part in line.split()]
        except ValueError:
            print(f"Skipping invalid line: {line}")
            continue

        sam = generate_samaccountname(first, last)
        base_upn = f"{first.lower()}.{last.lower()}@{DOMAIN}"
        upn = base_upn

        if upn in seen_upns:
            upn = f"{first.lower()}.{last.lower()}.{sam}@{DOMAIN}"
        seen_upns.add(upn)

        password = generate_password(WORD_LIST)
        users.append({
            'samAccountName': sam,
            'UPN': upn,
            'First Name': first,
            'Last Name': last,
            'Password': password
        })

        if len(users) >= limit:
            break

    return users

users = generate_users(raw_names, NUM_USERS)
with RESULTS_CSV_PATH.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=users[0].keys())
    writer.writeheader()
    writer.writerows(users)

print(f"{len(users)} users written to {RESULTS_CSV_PATH}")
