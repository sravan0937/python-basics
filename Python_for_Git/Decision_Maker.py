import tkinter as tk
import random

class DecisionApp:
    def __init__(self, root):
        self.themes = {
            "money": ["money", "salary", "investment", "profit", "income", "cash", "payment", "earn"],
            "love": ["love", "crush", "relationship", "feelings", "heart", "dating", "emotion", "romance"],
            "risk": ["risk", "danger", "loss", "gamble", "uncertain", "unsafe", "costly"],
            "opportunity": ["opportunity", "chance", "offer", "opening", "deal", "scope"],
            "confusion": ["confused", "unsure", "doubt", "stuck", "lost", "can't decide", "unclear"],
            "safety": ["safe", "secure", "stable", "guaranteed", "low risk", "reliable"],
            "career": ["job", "career", "resume", "internship", "interview", "apply", "work"],
            "health": ["health", "sick", "pain", "tired", "energy", "sleep", "medicine", "fit"],
            "study": ["study", "exam", "college", "assignment", "project", "focus", "learn"],
            "time": ["time", "late", "schedule", "wait", "rush", "now", "delay"]
        }

        self.response_sets = {
            "Chill": {
                "money": ["Looks good man, cash it in 😎", "Easy win. Don’t overthink it."],
                "love": ["Don’t stress. If it feels right, go for it.", "Vibe check: If it’s calm, proceed."],
                "risk": ["Bit sketchy, but hey… your call.", "Could work, could flop. Flip a coin 😅"],
                "opportunity": ["Why not? Give it a shot.", "Try it once, what’s the worst?"],
                "confusion": ["Grab a snack. Decide later.", "Confused? Just nap on it 😴"],
                "safety": ["Safe zone? Chill and cruise.", "Nothing wrong with playing it cool."],
                "career": ["Apply and move on. Don’t wait.", "It’s just a job, not marriage 🤷‍♂️"],
                "health": ["Rest up bro. Don’t break yourself.", "Hydrate and vibe. Health first."],
                "study": ["Focus for 30 mins, then chill.", "Grind now, binge later 🎮"],
                "time": ["You’re not late. World can wait.", "Clock? Ignore it. Flow with it."]
            },
            "Savage": {
                "money": ["Chase the bag or stay broke.", "You broke or what? Move."],
                "love": ["Feelings? Lol. Stay focused.", "Fall in love later. Get rich first."],
                "risk": ["Risky? Rise or cry later.", "You scared? Then don’t talk big."],
                "opportunity": ["Miss it and regret forever.", "One chance. Take it or shut up."],
                "confusion": ["Even your brain ditched you huh?", "Confused? Then you're not ready."],
                "safety": ["Safe is boring. You sure?", "Play it safe, live average."],
                "career": ["Apply now. Stop acting precious.", "Jobs don’t wait for babies."],
                "health": ["Fix your damn body first.", "Stop whining. Heal, then hustle."],
                "study": ["Books > excuses. Grind up.", "Cry now, top rank later."],
                "time": ["Wasting time talking. Move.", "Deadlines don’t care about your feelings."]
            },
            "Wise": {
                "money": ["Evaluate long-term gains before acting.", "Profit without clarity = regret later."],
                "love": ["Emotions matter, but don’t ignore logic.", "Patience reveals true intentions."],
                "risk": ["High risk demands high clarity.", "Weigh cost vs reward objectively."],
                "opportunity": ["Opportunities are doors. Don’t fear knocking.", "Consider timing and readiness."],
                "confusion": ["No clarity = No decision. Pause.", "Silence helps decode confusion."],
                "safety": ["Safe paths ensure stability. Choose wisely.", "Stability now allows risks later."],
                "career": ["Focus on skill, not just offers.", "Let your resume speak, not noise."],
                "health": ["Your body is your tool. Maintain it.", "No success without wellness."],
                "study": ["Knowledge builds silently. Trust process.", "Discipline today, success tomorrow."],
                "time": ["Every moment counts. Don’t waste it.", "Act on time, not on impulse."]
            }
        }

        self.root = root
        self.root.title("Decision-Maker App")

        self.input_box = tk.Text(root, height=5, width=50)
        self.input_box.pack(pady=10)

        self.tone_var = tk.StringVar(root)
        self.tone_var.set("Chill")
        self.tone_menu = tk.OptionMenu(root, self.tone_var, "Chill", "Savage", "Wise")
        self.tone_menu.pack(pady=5)

        self.submit_button = tk.Button(root, text="Get Decision", command=self.decide)
        self.submit_button.pack()

        self.output_box = tk.Text(root, height=10, width=50)
        self.output_box.pack(pady=10)

    def decide(self):
        text = self.input_box.get("1.0", tk.END).lower()
        tone = self.tone_var.get()
        responses = self.response_sets[tone]

        matched = []
        for theme, words in self.themes.items():
            for word in words:
                if word in text:
                    matched.append(theme)
                    break

        self.output_box.delete("1.0", tk.END)

        if matched:
            self.output_box.insert(tk.END, f"[{tone} Mode]\nLogic triggered from: {', '.join(matched)}\n\n")
            for m in matched:
                res = random.choice(responses[m])
                self.output_box.insert(tk.END, "- " + res + "\n")
        else:
            self.output_box.insert(tk.END, "🪫 No vibe detected.\nTry using more real-world words like: job, love, money, risk, etc.\n")
            self.output_box.insert(tk.END, "\n📌 Tip: Be honest. The app reacts to your intent, not formality.")

        self.input_box.delete("1.0", tk.END)
        self.output_box.see(tk.END)

# Run the app
root = tk.Tk()
app = DecisionApp(root)
root.mainloop()
