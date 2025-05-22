try:
    i = str(input())
    i = float(i)
    print(i)
except ValueError:
    print("数字を入力してください")
