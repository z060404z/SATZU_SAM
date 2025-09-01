import requests
import csv

csv_url = "https://urlhaus.abuse.ch/downloads/csv_recent/"

resp = requests.get(csv_url)
resp.raise_for_status()

lines = resp.text.splitlines()

lines = [line for line in lines if not line.startswith("#")]

if not lines:
    print("CSV 過濾後為空")
else:
    reader = csv.DictReader(lines)
    urls_written = 0
    with open("URLhaus_feed.txt", "w", encoding="utf-8") as f:
        for row in reader:
            url = row.get("url")
            if url:
                f.write(url.strip() + "\n")
                urls_written += 1
    print(f"已生成 URLhaus_feed.txt，共寫入 {urls_written} 條 URL")
