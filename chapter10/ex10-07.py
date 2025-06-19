def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\\     ",
             "|       / \\     ",
             "|               "
              ]

    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("".join(board))
    print("ハングマンへようこそ")
    while wrong < len(stages)-1:
        print("\n")
        msg = "1文字予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] =char
            rletters[cind] = '$'
        else:
            wrong += 1
        
        print(("".join(boad)))
        e =  wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("あなたの勝ち")
            print("".join(board))
            win = True
            break
