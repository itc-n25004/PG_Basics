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


    board = ["__"] * len(word)
    print("".join(board))

    while wrong < len(stages)-1:
        print("\n")
        msg = "1文字予想してね"
        char = input(msg)
        wrong += 1
        
        print(("".join(boad)))
        e =  wrong + 1
        print("\n".join(stages[0:e]))
