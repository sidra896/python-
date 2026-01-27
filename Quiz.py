
import tkinter as tk
import random

def start_quiz():
    quiz_win = tk.Toplevel(root)
    quiz_win.title("💖 Love Quiz for Sidra 💖")
    quiz_win.geometry("500x450")
    quiz_win.resizable(False, False)

    current_q = 0
    all_correct = True

    questions = [
        ("Sidra ke lye nickname kya use karte hoo ap?", "shazadi", "💖 Awww, thank you Shazady 💖"),
        ("Shaazadi se kitna pyar karte hooo ap?", "bhut zyada", "😍 Main bhi bohat zyada karti hoon 😍"),
        ("Shazadi ko kabhi choro ge to nahi?", "kabi nhi", "🤞 Hamesha saath rahenge InshaAllah 🤞")
    ]

    canvas = tk.Canvas(quiz_win, width=500, height=450, bg="#ffe6f0", highlightthickness=0)
    canvas.place(x=0, y=0)

    shapes = []
    colors = ["#ff1493", "#ff69b4", "#ffb6c1", "#c71585", "#db7093"]

    def create_shape():
        shape_type = random.choice(["💖", "🎈"])
        x = random.randint(30, 470)
        y = 440
        size = random.randint(15, 25)
        color = random.choice(colors)
        shape = canvas.create_text(x, y, text=shape_type, font=("Arial", size), fill=color)
        speed = random.randint(1, 4)
        shapes.append((shape, speed))
        quiz_win.after(400, create_shape)

    def move_shapes():
        for s, speed in shapes.copy():
            canvas.move(s, 0, -speed)
            coords = canvas.coords(s)
            if coords[1] < -20:
                canvas.delete(s)
                shapes.remove((s, speed))
        quiz_win.after(50, move_shapes)

    create_shape()
    move_shapes()

    frame = tk.Frame(quiz_win, bg="#fff0f5", bd=2, relief="ridge")
    frame.place(relx=0.5, rely=0.45, anchor="center")

    title = tk.Label(frame, text="💖 Love Quiz 💖", font=("Helvetica", 16, "bold"), bg="#fff0f5", fg="#c71585")
    title.pack(pady=5)

    q_label = tk.Label(frame, text="", font=("Helvetica", 12), wraplength=400, bg="#fff0f5")
    q_label.pack(pady=10)

    entry = tk.Entry(frame, font=("Helvetica", 12), width=30, bd=2, relief="groove")
    entry.pack(pady=5)

    btn = tk.Button(frame, text="Next", font=("Helvetica", 12, "bold"), bg="#ffb6c1", fg="white", relief="raised")
    btn.pack(pady=10)

    def heart_popup(message):
        pop = tk.Toplevel(quiz_win)
        pop.geometry("300x150")
        pop.resizable(False, False)
        pop.config(bg="#fff0f5")
        pop.title("💌 Message")

        pop_canvas = tk.Canvas(pop, width=300, height=150, bg="#fff0f5", highlightthickness=0)
        pop_canvas.pack()

        label = tk.Label(pop_canvas, text=message, font=("Helvetica", 12, "bold"), bg="#fff0f5", fg="#c71585")
        label.place(relx=0.5, rely=0.6, anchor="center")

        hearts = []

        def create_heart():
            x = random.randint(30, 270)
            y = 140
            size = random.randint(12, 18)
            color = random.choice(colors)
            heart = pop_canvas.create_text(x, y, text="💖", font=("Arial", size), fill=color)
            hearts.append(heart)
            pop.after(400, create_heart)

        def move_hearts():
            for heart in hearts.copy():
                pop_canvas.move(heart, 0, -2)
                coords = pop_canvas.coords(heart)
                if coords[1] < -20:
                    pop_canvas.delete(heart)
                    hearts.remove(heart)
            pop.after(50, move_hearts)

        create_heart()
        move_hearts()
        pop.after(2000, pop.destroy)

    def sparkle_final_text(canvas, text_id):
        scale = 1
        def animate():
            nonlocal scale
            scale += 0.05
            if scale > 1.3:
                scale = 1
            canvas.itemconfig(text_id, font=("Helvetica", int(20*scale), "bold"))
            quiz_win.after(100, animate)
        animate()

    def next_question():
        nonlocal current_q, all_correct
        user_ans = entry.get().strip().lower()

        if user_ans != questions[current_q][1]:
            all_correct = False
        else:
            heart_popup(questions[current_q][2])

        current_q += 1
        entry.delete(0, tk.END)

        if current_q == len(questions):
            frame.place_forget()
            title.config(text="")
            canvas.delete("all")

            if all_correct:
                final_msg = canvas.create_text(250, 220, text="💖 Love you sooo much 💖",
                                               font=("Helvetica", 20, "bold"), fill="#ff1493")
                sparkle_final_text(canvas, final_msg)
            else:
                canvas.create_text(250, 220, text="Dekhi… to pyar he nahi karta 💔",
                                   font=("Helvetica", 20, "bold"), fill="#ff0000")
        else:
            q_label.config(text=questions[current_q][0])

    btn.config(command=next_question)
    q_label.config(text=questions[0][0])

# Main window with only the clickable link
root = tk.Tk()
root.title("Love Quiz Link")
root.geometry("500x450")
root.configure(bg="#ffe6f0")

link_label = tk.Label(root, text="CLICK HERE TO START LOVE QUIZ", fg="#c71585",
                      bg="#ffe6f0", font=("Helvetica", 16, "bold"), cursor="hand2")
link_label.pack(expand=True, pady=200)

link_label.bind("<Button-1>", lambda e: start_quiz())

root.mainloop()
