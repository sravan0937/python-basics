# Themes with keyword groups
themes = {
    "money": ["money", "salary", "investment", "profit", "gain"],
    "love": ["love", "crush", "relationship", "feelings"],
    "risk": ["risk", "danger", "loss", "gamble"],
    "opportunity": ["opportunity", "chance", "offer"],
    "confusion": ["confused", "unsure", "doubt"],
    "safety": ["safe", "secure", "stable"]
}

# Responses per theme
responses = {
    "money": "Sounds profitable. Make sure you evaluate returns.",
    "love": "Matters of the heart? Don’t rush. Feelings > logic.",
    "risk": "Risk spotted. Proceed only if reward is worth it.",
    "opportunity": "Rare chances don’t wait. Go for it.",
    "confusion": "Clear your head. Don’t decide in confusion.",
    "safety": "If it feels safe, it probably is. Trust that."
}

# Input
situation = input("Tell me your situation: ").lower()

# Check for theme matches
matched = []
for theme, words in themes.items():
    for w in words:
        if w in situation:
            matched.append(theme)
            break  # avoid double count

# Final response
if matched:
    print("Decision logic triggered based on:", ", ".join(matched))
    for m in matched:
        print("-", responses[m])
else:
    print("No clear direction. Try rephrasing or give more detail.")
