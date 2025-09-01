import requests
import csv

csv_url = "https://urlhaus.abuse.ch/downloads/csv_recent/"

try:
    resp = requests.get(csv_url)
    resp.raise_for_status()
except Exception as e:
    print("抓取 CSV 失敗:", e)
    exit(1)

lines = resp.text.splitlines()
reader = csv.DictReader(lines)

urls_written = 0
with open("URLhaus_feed.txt", "w", encoding="utf-8") as f:
    for row in reader:
        url = row.get("url")
        if url:
            f.write(url + "\n")
            urls_written += 1

print(f"已生成 URLhaus_feed.txt，共寫入 {urls_written} 條 URL")
