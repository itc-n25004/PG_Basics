favorite_musician = {
        "1":"YOASOBI",
        "2":"米津玄師",
        "3":"Ado",
        "4":"ツユ",
        "5":"THE BINARY",
        "6":"Luna"
        }
n = input("数字を入力して下さい")
if n in favorite_musician:
    favorite_musician = favorite_musician[n]
    print(favorite_musician)
else:
    print("見つかりません")
