import random
fortune = ["大吉","吉","中吉","小吉","末吉","凶","大凶"]
kakuritu = [0.25,0.18,0.13,0.27,0.08,0.15,0.03]
kekka = random.choices(fortune,weights = kakuritu)
print(kekka)
