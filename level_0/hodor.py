#!/usr/bin/python
import requests
import time
from bs4 import BeautifulSoup

prox = {
    "https": "49.249.251.86:53281",
    "https": "101.109.255.18:36967",
    "https": "95.168.96.42:34273",
    "https": "193.117.138.126:46875",
    "https": "36.66.213.115:56488"
}


def verify_votes(id):
    r = requests.get("http://158.69.76.135/level0.php",
                     proxies=prox)
    votes = 0
    if r.status_code == 200:
        r.enconding = "utf-8"
        find = False
        soup = BeautifulSoup(r.content, "lxml")
        for tr in soup.table.find_all("tr"):
            i = 0
            for td in tr.find_all("td"):
                if td.get_text().strip() == str(id) and i == 0:
                    find = True
                if find and i == 1:
                    votes = int(td.get_text().strip())
                    find = False
                    break
                i = i + 1
    return (votes)


def do_vote(id):
    try:
        r = requests.post("http://158.69.76.135/level0.php",
                          data={"id": str(id), "holdthedoor": ""},
                          proxies=prox)
        if r.status_code == 200:
            print("Success vote :D!!")
            time.sleep(1)
    except Exception:
        print("It's not posible voting waiting ...")
        time.sleep(2)


if __name__ == "__main__":
    id = 953
    actual_votes = 0
    expected_votes = 1024
    while actual_votes != expected_votes:
        actual_votes = verify_votes(id)
        print("-" * 5)
        print(actual_votes)
        print("-" * 5)
        if actual_votes == expected_votes:
            print(f"Contratz you have {actual_votes}")
            break
        do_vote(id)
