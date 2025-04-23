
import random
import threading
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style


# Initialize styling
style = Style("cosmo")
root = style.master
root.title("Snake Water Gun")
root.geometry("400x500")

# Game data
choices = ['snake', 'water', 'gun']
rules = {
    "snake": "water",
    "water": "gun",
    "gun": "snake"
}
user_score = 0
comp_score = 0
MAX_SCORE = 5

# Sound helper
def play_sound(file):
    threading.Thread(target=play_sound, args=(file,), daemon=True).start()

# Reset the game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="")
    update_score()

# Update score label
def update_score():
    score_label.config(text=f"Score: You {user_score} - {comp_score} Computer")

# Game logic
def play(user_choice):
    global user_score, comp_score

    if user_score >= MAX_SCORE or comp_score >= MAX_SCORE:
        return  # Game over, do nothing

    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result_label.config(text=f"Draw! Both chose {user_choice}")
        play_sound("draw.wav")
    elif rules[user_choice] == comp_choice:
        user_score += 1
        result_label.config(text=f"You Win! Computer chose {comp_choice}")
        play_sound("win.wav")
    else:
        comp_score += 1
        result_label.config(text=f"You Lose! Computer chose {comp_choice}")
        play_sound("lose.wav")

    update_score()

    if user_score == MAX_SCORE:
        messagebox.showinfo("Game Over", "Congratulations! You WON the game!")
    elif comp_score == MAX_SCORE:
        messagebox.showinfo("Game Over", "Sorry! You LOST the game.")

# GUI Layout
tk.Label(root, text="Snake Water Gun", font=("Arial", 22, "bold")).pack(pady=15)
tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

for c in choices:
    tk.Button(
        btn_frame, text=c.capitalize(), font=("Arial", 14), width=10,
        command=lambda c=c: play(c), bg="#e0f7fa", relief="raised"
    ).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="black")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 14))
score_label.pack(pady=5)

tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game, bg="#dcedc8").pack(pady=15)

tk.Label(root, text="First to 5 wins!", font=("Arial", 11)).pack(pady=5)

root.mainloop()