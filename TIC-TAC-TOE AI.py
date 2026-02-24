import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic-Tac-Toe AI (Easy Mode)")
root.geometry("300x350")

board = [" " for _ in range(9)]
buttons = []

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# EASY AI (Random Move)
def ai_move():
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = "O"
        buttons[move].config(text="O")

# Button click
def on_click(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X")

        if check_winner("X"):
            messagebox.showinfo("Game Over", "You Win! 🎉")
            reset_game()
            return

        if is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
            return

        ai_move()

        if check_winner("O"):
            messagebox.showinfo("Game Over", "AI Wins 🤖")
            reset_game()
            return

        if is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()

# Reset game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text="")

# Create buttons
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 20),
                       width=5, height=2,
                       command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Restart button
restart_btn = tk.Button(root, text="Restart", command=reset_game)
restart_btn.grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()
