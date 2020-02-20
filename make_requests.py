"""
Laura Murphy
FE 595 - Webscraper
"""

import requests
import time
from bs4 import BeautifulSoup


def view_source(url):
    try:
        get_resp = requests.get(url)
    except:
        print("Request failed")
    return get_resp


def get_data(get_resp):
    soup = BeautifulSoup(get_resp.text, "html.parser")
    for elem in soup.find_all("li"):
        if elem.text.startswith("Name: "):
            name = elem.text[6:]
        if elem.text.startswith("Purpose: "):
            purpose = elem.text[9:]
    return [name, purpose]


def save(data, file):
    file.write(data[0] + "\t" + data[1] + "\n")


if __name__ == "__main__":
    f = open("companies.txt", "w")
    f.write("Name\tPurpose\n")
    for i in range(50):
        data = get_data(view_source("http://18.207.92.139:8000/random_company"))
        save(data, f)
        time.sleep(1)
    f.close()
