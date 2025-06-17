import csv

with open("challenge.txt", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["Top Gun","Riscky Business", "Minority Report"])
    w.writerow(["Taitanic", "The Revement", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])

with open("challenge.txt", "r", newline="") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

