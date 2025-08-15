import tkinter as tk
from tkinter import messagebox

questions = [
    ("What is the capital of India?", ["Mumbai", "New Delhi", "Kolkata"], "New Delhi"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter"], "Mars"),
    ("Who wrote the National Anthem of India?", ["Rabindranath Tagore", "Mahatma Gandhi", "Sarojini Naidu"], "Rabindranath Tagore"),
    ("How many states are there in India?", ["28", "29", "27"], "28"),
    ("What is the chemical symbol of water?", ["O2", "H2O", "CO2"], "H2O")
]

score = 0
q_index = 0

def check_answer(answer):
    global score, q_index
    if answer == questions[q_index][2]:
        score += 1
    q_index += 1
    if q_index < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Finished", f"Your Score: {score}/{len(questions)}")
def load_question():
    question_label.config(text=questions[q_index][0])
    for i, option in enumerate(questions[q_index][1]):
        option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x300")

question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12))
question_label.pack(pady=20)

option_buttons = []
for _ in range(3):
    btn = tk.Button(root, text="", width=20, font=("Arial", 10))
    btn.pack(pady=5)
    option_buttons.append(btn)

load_question()
root.mainloop()