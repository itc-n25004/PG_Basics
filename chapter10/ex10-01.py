def hangman(word):
    board = ["_"] * len(word)
    print("ハングマンへようこそ")
    print("".join(board))

hangman("cat")
