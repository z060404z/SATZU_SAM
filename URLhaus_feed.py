import requests
import csv

# URLhaus CSV 最近惡意 URL
csv_url = "https://urlhaus.abuse.ch/downloads/csv_recent/"

resp = requests.get(csv_url)
resp.raise_for_status()
lines = resp.text.splitlines()

reader = csv.DictReader(lines)

with open("urlhaus_feed.txt", "w", encoding="utf-8") as f:
    for row in reader:
        url = row.get("url")
        if url:
            f.write(url + "\n")

print("已生成 URLhaus_feed.txt")
