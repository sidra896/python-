import tkinter as tk
import random

# List of possible secret words
words = ["python", "developer", "computer", "keyboard", "internet", "programming", "hangman", "algorithm", "function", "variable"]

def start_game():
    game_win = tk.Toplevel(root)
    game_win.title("🎮 Ultimate Hangman Game")
    game_win.geometry("600x450")
    game_win.resizable(False, False)
    game_win.configure(bg="#1e1e2f")

    secret_word = random.choice(words)  # Random word every game
    guessed = []
    lives = 6
    score = 0
    display_word = ["_"] * len(secret_word)

    frame = tk.Frame(game_win, bg="#2a2a40", bd=3, relief="ridge")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    title = tk.Label(frame, text="🎯 ULTIMATE HANGMAN GAME", font=("Helvetica", 20, "bold"),
                     bg="#2a2a40", fg="#ffcc00")
    title.pack(pady=10)

    lives_label = tk.Label(frame, text="❤️ " * lives, font=("Helvetica", 16),
                           bg="#2a2a40", fg="#ff5c8a")
    lives_label.pack(pady=5)

    score_label = tk.Label(frame, text=f"Score: {score}", font=("Helvetica", 14),
                           bg="#2a2a40", fg="#00ffcc")
    score_label.pack(pady=5)

    word_label = tk.Label(frame, text=" ".join(display_word), font=("Consolas", 28, "bold"),
                          bg="#2a2a40", fg="#00ffcc")
    word_label.pack(pady=20)

    entry = tk.Entry(frame, font=("Helvetica", 16), width=5, justify="center",
                     bd=2, relief="solid")
    entry.pack(pady=5)

    msg_label = tk.Label(frame, text="", font=("Helvetica", 12),
                         bg="#2a2a40", fg="#ff6666")
    msg_label.pack(pady=5)

    # Optional: show vowels as hint
    vowels_label = tk.Label(frame, text="Vowels hint: a, e, i, o, u", font=("Helvetica", 10, "italic"),
                            bg="#2a2a40", fg="#ffb347")
    vowels_label.pack(pady=5)

    def end_game(win):
        entry.config(state="disabled")
        if win:
            msg_label.config(text=f"🎉 You Win! Word: {secret_word} 💖", fg="#00ffcc")
        else:
            msg_label.config(text=f"💀 Game Over! Word was: {secret_word}", fg="#ff4444")

        restart_btn = tk.Button(frame, text="🔄 Restart Game", font=("Helvetica", 14, "bold"),
                                bg="#ffcc00", fg="#1e1e2f",
                                activebackground="#ffaa00", activeforeground="white",
                                padx=15, pady=5,
                                command=lambda: [game_win.destroy(), start_game()])
        restart_btn.pack(pady=10)

    def guess_letter():
        nonlocal lives, score
        letter = entry.get().lower()
        entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            msg_label.config(text="⚠️ Enter only 1 letter!", fg="#ff6666")
            return

        if letter in guessed:
            msg_label.config(text="🔁 Letter already guessed!", fg="#ff6666")
            return

        guessed.append(letter)

        if letter in secret_word:
            count = 0
            for i, ch in enumerate(secret_word):
                if ch == letter:
                    display_word[i] = letter
                    count += 1
            word_label.config(text=" ".join(display_word))
            score += count * 10  # 10 points per correct letter
            score_label.config(text=f"Score: {score}")
            msg_label.config(text=f"✔️ Correct guess! (+{count*10} points)", fg="#66ff66")
        else:
            lives -= 1
            lives_label.config(text="❤️ " * lives)
            msg_label.config(text="❌ Wrong guess!", fg="#ff6666")

        if "_" not in display_word:
            end_game(win=True)
        elif lives == 0:
            end_game(win=False)

    btn = tk.Button(frame, text="GUESS", command=guess_letter,
                    font=("Helvetica", 14, "bold"),
                    bg="#ffcc00", fg="#1e1e2f",
                    activebackground="#ffaa00", activeforeground="white",
                    padx=20, pady=5)
    btn.pack(pady=10)


# Main window
root = tk.Tk()
root.title("🎮 Game Hub")
root.geometry("600x450")
root.configure(bg="#1e1e2f")

start_btn = tk.Button(root, text="🎮 START ULTIMATE HANGMAN GAME", font=("Helvetica", 16, "bold"),
                      bg="#00ffcc", fg="#1e1e2f",
                      activebackground="#00ccaa", activeforeground="white",
                      padx=20, pady=10,
                      command=start_game)
start_btn.pack(expand=True)

root.mainloop()
