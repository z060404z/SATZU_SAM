import requests
import csv
import sys

csv_url = "https://urlhaus.abuse.ch/downloads/csv_recent/"

try:
    resp = requests.get(csv_url)
    resp.raise_for_status()
except Exception as e:
    print("抓取 CSV 失敗:", e)
    sys.exit(1)

lines = resp.text.splitlines()
reader = csv.DictReader(lines)

with open("URLhaus_feed.txt", "w", encoding="utf-8") as f:
    for row in reader:
        url = row.get("url")
        if url:
            f.write(url + "\n")

print("已生成 URLhaus_feed.txt")
