# Step 1: Get situation
situation = input("Tell me your situation: ")

# Define keywords and their scores
keywords = {
    "money": 2,
    "love": -1,
    "risk": -2,
    "opportunity": 3,
    "urgent": -1,
    "safe": 2,
    "loss": -3,
    "gain": 3,
    "confused": -1
}

# Analyze situation
score = 0
for word in keywords:
    if word in situation.lower():
        score += keywords[word]

# Give decision
if score >= 3:
    decision = "Do it. No regrets."
elif score >= 1:
    decision = "Seems fine, but think once."
elif score == 0:
    decision = "Too neutral. Need more info."
else:
    decision = "Avoid it. Smells like trouble."

print("Decision:", decision)
