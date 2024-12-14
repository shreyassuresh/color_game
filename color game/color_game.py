import tkinter as tk
import random

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink', 'Black', 'White', 'Brown']

def next_question():
    global score
   
    color_name = random.choice(colors)
    display_color = random.choice(colors)

    question_label.config(text=color_name, fg=display_color)
    current_color.set(display_color)
    # Set the answer options
    color_buttons[0].config(text=colors[0], bg=colors[0])
    color_buttons[1].config(text=colors[1], bg=colors[1])
    color_buttons[2].config(text=colors[2], bg=colors[2])
    color_buttons[3].config(text=colors[3], bg=colors[3])

def check_answer(selected_color):
    global score
    
    if selected_color == current_color.get():
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text="Wrong!", fg="red")
    
    score_label.config(text=f"Score: {score}")
    next_question()

root = tk.Tk()
root.title("Color Game")

score = 0
current_color = tk.StringVar()

question_label = tk.Label(root, font=('Helvetica', 30), width=20)
question_label.pack(pady=50)

score_label = tk.Label(root, text=f"Score: {score}", font=('Helvetica', 20))
score_label.pack()

color_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=('Helvetica', 20), width=15, height=2,
                       command=lambda color=colors[i]: check_answer(color))
    button.pack(pady=10)
    color_buttons.append(button)

feedback_label = tk.Label(root, font=('Helvetica', 20))
feedback_label.pack(pady=20)

next_question()

root.mainloop()
