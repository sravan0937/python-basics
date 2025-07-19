import tkinter as tk

class DecisionApp:
    def __init__(self, root):
        self.themes = {
            "money": ["money", "salary", "investment", "profit", "gain"],
            "love": ["love", "crush", "relationship", "feelings"],
            "risk": ["risk", "danger", "loss", "gamble"],
            "opportunity": ["opportunity", "chance", "offer"],
            "confusion": ["confused", "unsure", "doubt"],
            "safety": ["safe", "secure", "stable"]
        }

        self.responses = {
            "money": "Sounds profitable. Make sure you evaluate returns.",
            "love": "Matters of the heart? Don’t rush. Feelings > logic.",
            "risk": "Risk spotted. Proceed only if reward is worth it.",
            "opportunity": "Rare chances don’t wait. Go for it.",
            "confusion": "Clear your head. Don’t decide in confusion.",
            "safety": "If it feels safe, it probably is. Trust that."
        }

        self.root = root
        self.root.title("Decision-Maker App")

        self.input_box = tk.Text(root, height=5, width=50)
        self.input_box.pack(pady=10)

        self.submit_button = tk.Button(root, text="Get Decision", command=self.decide)
        self.submit_button.pack()

        self.output_box = tk.Text(root, height=10, width=50)
        self.output_box.pack(pady=10)

    def decide(self):
        text = self.input_box.get("1.0", tk.END).lower()
        matched = []

        for theme, words in self.themes.items():
            for word in words:
                if word in text:
                    matched.append(theme)
                    break

        self.output_box.delete("1.0", tk.END)

        if matched:
            self.output_box.insert(tk.END, "Logic triggered based on: " + ", ".join(matched) + "\n\n")
            for m in matched:
                self.output_box.insert(tk.END, "- " + self.responses[m] + "\n")
        else:
            self.output_box.insert(tk.END, "No clear direction. Rephrase or add detail.")

# Run app
root = tk.Tk()
app = DecisionApp(root)
root.mainloop()
