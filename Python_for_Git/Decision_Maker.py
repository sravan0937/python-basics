import tkinter as tk

# Logic setup
themes = {
    "money": ["money", "salary", "investment", "profit", "gain"],
    "love": ["love", "crush", "relationship", "feelings"],
    "risk": ["risk", "danger", "loss", "gamble"],
    "opportunity": ["opportunity", "chance", "offer"],
    "confusion": ["confused", "unsure", "doubt"],
    "safety": ["safe", "secure", "stable"]
}

responses = {
    "money": "Sounds profitable. Make sure you evaluate returns.",
    "love": "Matters of the heart? Don’t rush. Feelings > logic.",
    "risk": "Risk spotted. Proceed only if reward is worth it.",
    "opportunity": "Rare chances don’t wait. Go for it.",
    "confusion": "Clear your head. Don’t decide in confusion.",
    "safety": "If it feels safe, it probably is. Trust that."
}

# Function to process input
def decide():
    text = input_box.get("1.0", tk.END).lower()
    matched = []
    for theme, words in themes.items():
        for w in words:
            if w in text:
                matched.append(theme)
                break
    output_box.delete("1.0", tk.END)
    if matched:
        output_box.insert(tk.END, "Logic triggered based on: " + ", ".join(matched) + "\n\n")
        for m in matched:
            output_box.insert(tk.END, "- " + responses[m] + "\n")
    else:
        output_box.insert(tk.END, "No clear direction. Rephrase or add detail.")

# GUI Setup
window = tk.Tk()
window.title("Decision-Maker 1.0")

input_box = tk.Text(window, height=5, width=50)
input_box.pack(pady=10)

submit_button = tk.Button(window, text="Get Decision", command=decide)
submit_button.pack()

output_box = tk.Text(window, height=10, width=50)
output_box.pack(pady=10)

window.mainloop()
