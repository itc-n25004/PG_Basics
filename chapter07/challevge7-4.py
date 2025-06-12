q = [7,11,13,1001]
i = 0
while True:
    number_quiz = input("数字をいれてください")
    if "q" == number_quiz:
        break
    try:
        number_quiz = int(number_quiz)
    except ValueError:
        print("数字を入力するか、ｑを入れてくだいさい")
    if number_quiz in q:
        print("正解")
        break
    else:
        print("不正解")
