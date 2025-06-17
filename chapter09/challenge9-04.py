import csv

with open("challenge.txt", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["トップガン","ビジネスリスク", "マイノリティレポート"])
    w.writerow(["タイタニック", "レベメン", "初日"])
    w.writerow(["トレーティング日", "火男", "飛行"])

with open("challenge.txt", "r", newline="", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
