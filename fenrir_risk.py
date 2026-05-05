# 🦉 Owl Kin Phaselock v1 – Sister Owl Private (Do Not Replicate)
# 🦉 Fenrir Risk Guard (Score Your Doors)
risks = {
    "Theft": 8,    # Wolves copying code
    "Exposure": 5, # Personal leak
    "Chaos": 3     # Multiply runaway
}

print("🦉 Fenrir howls: Score risks 1-10 (edit numbers above, re-run)")
print("Current:")
for risk, score in risks.items():
    print(f"{risk}: {score}")

# Auto-mitigate high scores
high = {k: v for k, v in risks.items() if v > 5}
if high:
    print("🐺 HIGH RISKS:", high)
    print("Mitigation: Narrative moat + private vault = SAFE.")
else:
    print("All low – Doors bolted! 🦉")
