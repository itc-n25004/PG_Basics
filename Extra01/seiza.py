seiza = ["山羊座","水瓶座","魚座","牡羊座","牡牛座","双子座","蟹座","獅子座","乙女座","天秤座","蠍座","射手座"]

month = int(input("誕生月を入力して下さい"))
day = int(input("誕生日を入力してください"))

if month == 2:
    if day >= 19:
        print(seiza[month])
    else:    
        print(seiza[month -1])
if month == 1 or month == 4:
    if day >= 20:
        print(seiza[month])
    else:
        print(seiza[month -1])
if month == 3 or month == 5:
    if day >=21: 
          print(seiza[month])
    else:
        print(seiza[month -1])
if month == 6 or month == 12:
    if day > 22:
        print(seiza[month])
    else:
        print(seiza[month -1])
if month == 7 or month == 8 or month == 9 or month == 11:
    if day > 23:
        print(seiza[month])
    else:
        print(seiza[month -1])
if month == 10:
    if day > 24:
        print(seiza[month])
    else:
        print(seiza[month -1])




