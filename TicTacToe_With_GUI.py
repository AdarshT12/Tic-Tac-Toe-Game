import tkinter as tk
from tkinter import messagebox

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
win = 1
draw = -1
running = 0
stop = 1
game = running
mark = 'X'

def draw_board():
    for i in range(1, 10):
        button = tk.Button(root, text=board[i], font=('normal', 20), width=5, height=2, command=lambda i=i: on_click(i))
        button.grid(row=(i - 1) // 3, column=(i - 1) % 3)

def check_position(x):
    return board[x] == ' '

def check_win():
    global game
    for i in range(0, 3):
        if board[i * 3 + 1] == board[i * 3 + 2] == board[i * 3 + 3] != ' ':
            game = win
    for i in range(0, 3):
        if board[i + 1] == board[i + 4] == board[i + 7] != ' ':
            game = win
    if board[1] == board[5] == board[9] != ' ' or board[3] == board[5] == board[7] != ' ':
        game = win
    if ' ' not in board[1:]:
        game = draw

def reset_game():
    global board, player ,game , mark
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 1
    game = running
    mark = 'X'
    draw_board()

def on_click(choice):
    global player, mark, game
    if check_position(choice) and game == running:
        board[choice] = mark
        draw_board()
        check_win()
        if game == win:
            messagebox.showinfo("Tic-Tac-Toe", f"Player {1 if player % 2 != 0 else 2} won!")
            reset_game()
        elif game == draw:
            messagebox.showinfo("Tic-Tac-Toe", "Game Draw")
            reset_game()
        else:
            player = 3 - player
            mark='X'if player == 1 else '0'
            print("Tic-Tac-Toe",f"Player {player}'s chance")


root = tk.Tk()
root.title("Tic-Tac-Toe")

label = tk.Label(root, text="Player 1[X]---Player 2[0]", font=('normal', 16))
label.grid(row=0, column=0, columnspan=3)

draw_board()

root.mainloop()
