import tkinter as tk
import random
import threading

choices = ["snake", "water", "gun"]

def play_sound(file):
    threading.Thread(target=play_sound, args=(file,), daemon=True).start()

def decide(user):
    comp = random.choice(choices)
    result = ""

    if user == comp:
        result = f"Draw! Both chose {user}"
        play_sound("draw.wav")
    elif (user == "snake" and comp == "water") or \
         (user == "water" and comp == "gun") or \
         (user == "gun" and comp == "snake"):
        result = f"You Win! Computer chose {comp}"
        play_sound("win.wav")
    else:
        result = f"You Lose! Computer chose {comp}"
        play_sound("lose.wav")

    result_label.config(text=result)

# GUI
root = tk.Tk()
root.title("Snake Water Gun")
root.geometry("300x300")
root.config(bg="lightblue")

tk.Label(root, text="Choose:", font=("Arial", 16), bg="lightblue").pack(pady=10)

for choice in choices:
    tk.Button(root, text=choice.capitalize(), font=("Arial", 14),
              command=lambda c=choice: decide(c)).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)

root.mainloop()