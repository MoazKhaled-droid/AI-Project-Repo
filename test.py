def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("-" * 10)
print_board()