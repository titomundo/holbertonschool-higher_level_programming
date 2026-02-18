#!/usr/bin/python3

"""task_02_requests:
Use the requests module in python to fetch and store data from an API
"""

import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts/")
    print(f"Status Code: {r.status_code}")
    jdata = r.json()

    for entry in jdata:
        print(entry["title"])


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts/")

    with open("posts.csv", "w", encoding="utf-8", newline="") as csvfile:
        jdata = r.json()
        headers = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, headers)

        writer.writeheader()

        for entry in jdata:
            entry.pop("userId")
            writer.writerow(entry)
