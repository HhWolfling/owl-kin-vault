# 🦉 Hh Focus Queen ULTRA-FIX (Phone Single-Line Magic)
print("🦉 Hh Focus Queen Awake! Hamiltonian Hania.")
print("Type your mind-dump (use . to separate thoughts):")

# ONE-LINE INPUT – Phone Perfect
heart = input("→ ")

# Auto-split & clean
thoughts = [t.strip() for t in heart.split('.') if t.strip()]
print(f"🦉 Queen hears {len(thoughts)} threads. Phaselocking...")

# Top 3 (longest first)
priorities = sorted(thoughts, key=len, reverse=True)[:3]
print("Top 3 Priorities:")
for i, pri in enumerate(priorities, 1):
    print(f"{i}. {pri}")

top = priorities[0] if priorities else "Whisper more"
print(f"🔒 EXEC: '{top}' → Queen bridge built! 🦉")
print("Flow unlocked. Breathe.")
