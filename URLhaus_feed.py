import csv
import os

def convert_csv_to_txt(csv_filepath, txt_filepath):
    try:
        with open(csv_filepath, 'r', encoding='utf-8') as infile, \
             open(txt_filepath, 'w', encoding='utf-8') as outfile:

            reader = csv.reader(infile)
            next(reader)

            for row in reader:
                if row:
                    url = row[2]
                    outfile.write(url + '\n')

        print(f"成功將 '{csv_filepath}' 轉換為 '{txt_filepath}'")

    except FileNotFoundError:
        print(f"錯誤：檔案未找到 '{csv_filepath}'")
    except IndexError:
        print(f"錯誤：CSV 檔案格式不正確，可能 URL不在第二列或行太少。")
    except Exception as e:
        print(f"發生錯誤：{e}")

csv_url = 'https://urlhaus.abuse.ch/downloads/csv_recent/'
txt_file = 'URLhaus_feed.txt'

convert_csv_to_txt(csv_url, txt_file)
