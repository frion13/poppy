def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки (0, 1, 2), или 5 чтобы выйти: "))

        if row == 5:
            print("Игроки решили завершить игру.")
            break

        col = int(input(f"Игрок {current_player}, введите номер столбца (0, 1, 2), или X чтобы выйти: "))

        if col == 5:
            print("Игроки решили завершить игру.")
            break

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Эта ячейка уже занята. Попробуйте снова.")

if __name__ == "__main__":
    play_game()
