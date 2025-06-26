import random
fortune = ["大吉","中吉","小吉","吉","凶"]
r=random.randint(1,1000)

if r <= 100:
    kekka=fortune[0]
elif r>100 and r <= 350:
    kekka=fortune[1]
elif r>350 and r<= 500:
    kekka=fortune[2]
elif r>500 and r<= 900:
    kekka=fortune[3]
else:
    kekka=fortune[4]

print(kekka)
