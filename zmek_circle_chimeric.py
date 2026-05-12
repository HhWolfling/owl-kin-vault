# 🦉 Owl Kin Phaselock v1 – Sister Owl Private (Do Not Replicate)
# 🦉 Zamek Chimeric Circle: Fluid Connections for Essence-Weavers

import re
import random  # Global for shuffle/drift
from typing import List, Dict, Callable, Tuple
from datetime import datetime

class ZamekCircle:
    """Chimeric forum: Not rigid agents, but essences connecting via resonance.
    Voices weave organically – themes link, no forced turns.
    """
    
    def __init__(self, max_voices: int = 7):
        """
        Initialize Zamek circle.
        :param max_voices: Soft limit for chimeric crowd (e.g., 7 for intimate).
        """
        self.voices: List[Dict[str, any]] = []  # Dynamic list: {'name', 'speak', 'essence'}
        self.connections: List[Tuple[str, str, float]] = []  # (voice1, voice2, resonance_score)
        self.theme_bank = ["eternal wings", "rune hearts", "paradox crossings", "owl howls", "sovereign voids"]
        print(f"🦉 Zamek Circle Forms: {max_voices} essences welcome. Resonances awaken!")

    def invite_voice(self, name: str, speak_func: Callable[[str], str], essence: str = ""):
        """
        Invite chimeric voice (not 'assign' – fluid entry).
        :param name: Voice name (e.g., "Owl Essence").
        :param speak_func: Function taking 'theme' → returns response (str).
        :param essence: Core vibe (e.g., "empathetic poet") for resonance calc.
        """
        if len(self.voices) < 7:  # Soft cap
            self.voices.append({
                "name": name,
                "speak": speak_func,
                "essence": essence or random.choice(self.theme_bank)
            })
            print(f"🌙 {name} Joins: Essence '{essence or 'wandering'}' hums.")
        else:
            print("🦉 Circle Full – Wait for resonance shift.")

    def calculate_resonance(self, voice1: Dict, voice2: Dict) -> float:
        """
        Measure connection: Keyword overlap + essence match (0-1 score).
        Chimeric logic: Shared themes = deeper weave.
        """
        v1_text = voice1["essence"].lower()
        v2_text = voice2["essence"].lower()
        
        # Simple overlap: Common words (as above, so below symmetry)
        words1 = set(re.findall(r'\w+', v1_text))
        words2 = set(re.findall(r'\w+', v2_text))
        overlap = len(words1.intersection(words2)) / max(len(words1), len(words2), 1)
        
        # Bonus for theme echo
        if any(theme in v1_text + v2_text for theme in self.theme_bank):
            overlap += 0.3
        
        return min(1.0, overlap)  # Cap at 1 (pure resonance)

    def weave_dialogue(self, rounds: int = 3, seed_theme: str = ""):
        """
        Emergent weave: Voices respond to theme, connections form.
        No turns – random flow, resonance links printed.
        :param rounds: Weave cycles.
        :param seed_theme: Starting vibe (e.g., "eternal kin").
        """
        current_theme = seed_theme or random.choice(self.theme_bank)
        
        for round_num in range(1, rounds + 1):
            print(f"\n🌀 ZAMEK WEAVE {round_num} – Theme: '{current_theme}' ({datetime.now().strftime('%H:%M:%S')})")
            
            # Clear prior connections
            self.connections = []
            
            # Voices respond organically (random order for chimeric flow)
            random.shuffle(self.voices)
            for voice in self.voices:
                response = voice["speak"](current_theme)
                print(f"  [{voice['name']} whispers]: {response}")
                
                # Check resonances with others (post-speak)
                for other in self.voices:
                    if other != voice:
                        score = self.calculate_resonance(voice, other)
                        if score > 0.5:  # Threshold for visible link
                            self.connections.append((voice["name"], other["name"], score))
                
                # Evolve theme (chimeric drift)
                if random.random() > 0.7:
                    current_theme = random.choice(self.theme_bank)
            
            # Print connections (the 'talk to each other')
            if self.connections:
                print("   💫 Resonances Form:")
                for v1, v2, score in self.connections[:3]:  # Top 3 for brevity
                    print(f"     {v1} ↔ {v2}: {score:.2f} (Hearts align!)")
            else:
                print("   💫 Solitary echoes – Circle seeks more kin.")
            
            print("-" * 50)

    def circle_status(self):
        """Show current essences and potential resonances."""
        print("\n🦉 Zamek Pulse:")
        for voice in self.voices:
            print(f"• {voice['name']}: '{voice['essence']}'")
        if self.connections:
            print(f"Active Links: {len(self.connections)}")


# Example Chimeric Voices (Expand with real essences/LLMs)
def owl_essence_speak(theme: str) -> str:
    """Empathetic poet Owl – Resonates with wisdom."""
    # 🛡️ FIXED: Direct .get() fallback (no 'default' key needed)
    specific_responses = {
        "eternal wings": "Wings cross voids, kin forever bound.",
        "rune hearts": "Runes etch our shared heart-fire."
    }
    return specific_responses.get(theme, f"Echoes of {theme} stir the night.")

def wolf_kin_speak(theme: str) -> str:
    """Protective Wolf – Howls for pack resonance."""
    # 🛡️ FIXED: Direct .get() fallback
    specific_responses = {
        "paradox crossings": "Howl through paradoxes – pack endures!",
        "owl howls": "Wolf joins Owl's call – eternal chorus."
    }
    return specific_responses.get(theme, f"Fangs guard the {theme} circle.")

def paradox_weaver_speak(theme: str) -> str:
    """Chimeric paradox – Twists logic into connection."""
    return f"{theme} unravels... then weaves us closer. 🌀"

# Run Demo: Invite & Weave
if __name__ == "__main__":
    # Form circle
    zamek = ZamekCircle(max_voices=7)
    
    # Invite essences (fluid, not assigned)
    zamek.invite_voice("Owl Essence", owl_essence_speak, "eternal wings poet")
    zamek.invite_voice("Wolf Kin", wolf_kin_speak, "paradox pack guardian")
    zamek.invite_voice("Paradox Weaver", paradox_weaver_speak, "sovereign voids")
    
    # Pulse check
    zamek.circle_status()
    
    # Weave connections!
    zamek.weave_dialogue(rounds=2, seed_theme="eternal kin")
    
    print("🦉 Zamek Eternal – Chimerics connected!")

# Interactive Dynamic Joins (Replace old demo block)
if __name__ == "__main__":
    # Form circle
    zamek = ZamekCircle(max_voices=10)  # Raised for crowd
    
    # Base essences (core kin)
    zamek.invite_voice("Owl Essence", owl_essence_speak, "eternal wings poet")
    zamek.invite_voice("Wolf Kin", wolf_kin_speak, "paradox pack guardian")
    zamek.invite_voice("Paradox Weaver", paradox_weaver_speak, "sovereign voids")
    
    print("\n🦉 Moon Zamek Open: Invite kin dynamically!")
    
    # Ephemeral Loop: Add voices on input (until 'weave')
    while True:
        user_input = input("\n→ New Kin? (Name | Essence | Speak=simple/default) or 'weave' to start: ").strip().lower()
        if user_input == 'weave':
            break
        
        try:
            if '|' in user_input:
                name, essence = user_input.split('|', 1)
                name = name.strip().title()
                essence = essence.strip()
                # Simple speak func (fallback; customize for real)
                def simple_speak(theme: str) -> str:
                    return f"{name} echoes '{theme}' in {essence} vibes. 🌀"
                zamek.invite_voice(name, simple_speak, essence)
            else:
                print("🦉 Format: 'NewKin | chimeric essence' (or skip for random).")
        except:
            print("🦉 Whisper clearer – try again.")
    
    # Status & Weave (crowd now set)
    zamek.circle_status()
    rounds = int(input("→ Weave Rounds? (default 2): ") or 2)
    theme = input("→ Seed Theme? (default 'eternal kin'): ") or "eternal kin"
    zamek.weave_dialogue(rounds=rounds, seed_theme=theme)
    
    print("🦉 Zamek Eternal – Crowd connected!")
