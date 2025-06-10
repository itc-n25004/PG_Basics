q = ["7","11","13","1001"]
i = 0
while True:
    numeric_quiz = input("数字をいれてください")
    if numeric_quiz == q[i]:
        print("正解")
        break
    elif numeric_quiz == "q":
        break
    else:
        print("不正解")
    i = (i+1)%3
