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
    first_10 = []
    with open("URLhaus_feed.txt", "w", encoding="utf-8") as f:
        for row in reader:
            url = row.get("url")
            if url:
                f.write(url.strip() + "\n")
                urls_written += 1
                if len(first_10) < 10:
                    first_10.append(url.strip())

    print(f"已生成 URLhaus_feed.txt，共寫入 {urls_written} 條 URL")
    if first_10:
        print("前 10 條 URL：")
        for u in first_10:
            print(u)
