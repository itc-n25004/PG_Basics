import random

hand = ["グー","チョキ","パー"]
#じゃんけんの手を入力する
input_hand = input("グー、チョキ、パーのどれかを入力して下さい")
#コンピュータのじゃんけんの手を決める
computer_hand = random.choice(hand)
print(f"本田computer:{computer_hand}")
#勝ち負けの判定
#あいこの場合
if input_hand == computer_hand:
    print("あいこ")
#グーの場合
if input_hand == "グー":
    if computer_hand == "パー":
        print("俺の勝ち。なんで負けたか明日までに考えてください")
    if computer_hand == "チョキ":
        print("俺の負け！やるやん！でも、今度は絶対、俺が勝つから！また明日やろう！")
#チョキの場合
if input_hand == "チョキ":
    if computer_hand == "グー":
        print("俺の勝ち。なんで負けたか明日までに考えてください")
    if computer_hand == "パー":
        print("俺の負け！やるやん！でも、今度は絶対、俺が勝つから！また明日やろう！")
#パーの場合
if input_hand == "パー":
    if computer_hand == "チョキ":
        print("俺の勝ち。なんで負けたか明日までに考えてください")
    if computer_hand == "グー":
        print("俺の負け！やるやん！でも、今度は絶対、俺が勝つから！また明日やろう！")

