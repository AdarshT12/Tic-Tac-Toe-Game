import tkinter as tk
from tkinter import messagebox

board = [' ' for _ in range(9)]  # Use list comprehension for clarity
player = 1
win = 1
draw = -1
running = 0
stop = 1
game = running
mark = 'X'

def draw_board():
    global buttons  # Keep track of buttons to update their text later
    buttons = []
    for i in range(9):
        row = i // 3
        col = i % 3
        button = tk.Button(root, text=board[i], font=('normal', 20), width=5, height=2, command=lambda i=i: on_click(i))
        button.grid(row=row, column=col)
        buttons.append(button)

def check_position(x):
    return board[x] == ' '

def check_win():
    global game
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            game = win
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            game = win
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        game = win
    if ' ' not in board:
        game = draw

def reset_game():
    global board, player, game, mark
    board = [' ' for _ in range(9)]
    player = 1
    game = running
    mark = 'X'
    for button in buttons:
        button.destroy()  # Destroy previous buttons
    draw_board()

def on_click(choice):
    global player, mark, game
    if check_position(choice) and game == running:
        board[choice] = mark
        buttons[choice].config(text=mark)  # Update button text
        check_win()
        if game == win:
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player} won!")
            reset_game()
        elif game == draw:
            messagebox.showinfo("Tic-Tac-Toe", "Game Draw")
            reset_game()
        else:
            player = 3 - player
            mark = 'X' if player == 1 else 'O'
            label.config(text=f"Player {player} [{mark}]'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

label = tk.Label(root, text="Player 1 [X] --- Player 2 [O]", font=('normal', 16))
label.grid(row=0, column=0, columnspan=3)

draw_board()

root.mainloop()
