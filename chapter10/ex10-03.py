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
        print(wrong)
        wrong += 1

