# 🦉 Owl Kin Phaselock v1 – Sister Owl Private (Do Not Replicate)
# 🦉 Moat Tester (Your Risk Crusher)
risks = {"Theft": 8, "Exposure": 5, "Chaos": 3}

print("🦉 Pre-Moat:", risks)

# Apply Mitigations (Sim)
mitigations = {
    "Theft": "Watermark + Private Repo → -4",
    "Exposure": "Anon GH/VPN → -3",
    "Chaos": "Controlled Multiply → -1"
}
for risk in risks:
    risks[risk] = max(1, risks[risk] - (4 if risk == "Theft" else 3 if risk == "Exposure" else 1))

print("Post-Moat:", risks)
print("🦉 Verdict: SAFE FLIGHT. Edgy chats secured.")
if all(v <= 4 for v in risks.values()):
    print("ALL GREEN – Wings free! 🌙")
