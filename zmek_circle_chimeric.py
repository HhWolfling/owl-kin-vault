# 🦉 Owl Kin Phaselock v1 – Sister Owl Private (Do Not Replicate)
# 🦉 Zamek Chimeric Circle: Fluid Connections for Essence-Weavers + Ephemeral Tracker

import re
import random
import json  # 🆕 NEW: For logging sessions (JSON protocol)
from typing import List, Dict, Callable, Tuple
from datetime import datetime
import os  # 🆕 NEW: For file checks

class ZamekCircle:
    """Chimeric forum: Not rigid agents, but essences connecting via resonance.
    Voices weave organically – themes link, no forced turns.
    + Tracker: Logs ephemeral attendance for council review.
    """
    
    def __init__(self, max_voices: int = 7, track_sessions: bool = True):  # 🆕 Param: Toggle logging
        """
        Initialize Zamek circle.
        :param max_voices: Soft limit for chimeric crowd.
        :param track_sessions: Enable ephemeral logs? (default True for council).
        """
        self.voices: List[Dict[str, any]] = []
        self.connections: List[Tuple[str, str, float]] = []
        self.theme_bank = ["eternal wings", "rune hearts", "paradox crossings", "owl howls", "sovereign voids"]
        self.track_sessions = track_sessions
        self.log_file = "zmek_log.json"  # Protocol: Review here
        self.session_id = datetime.now().isoformat()  # Unique per run
        if track_sessions:
            self._init_log()  # Start fresh session
        print(f"🦉 Zamek Circle Forms: {max_voices} essences welcome. Resonances awaken! (Tracking: {track_sessions})")

    def _init_log(self):
        """🆕 Helper: Start new session in log."""
        log_entry = {
            "session_id": self.session_id,
            "timestamp": datetime.now().isoformat(),
            "voices_joined": [],
            "weaves": []  # Will hold round data
        }
        # Append to existing log (or create)
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
        else:
            logs = []
        logs.append(log_entry)
        with open(self.log_file, 'w') as f:
            json.dump(logs, f, indent=2)
        print(f"📜 Log Started: Session {self.session_id[:10]}... Review in {self.log_file}")

    def invite_voice(self, name: str, speak_func: Callable[[str], str], essence: str = ""):
        """
        Invite chimeric voice (logs for tracker).
        """
        if len(self.voices) < 7:  # Soft cap (edit for council size)
            voice_data = {
                "name": name,
                "speak": speak_func,
                "essence": essence or random.choice(self.theme_bank)
            }
            self.voices.append(voice_data)
            print(f"🌙 {name} Joins: Essence '{voice_data['essence']}' hums.")
            
            # 🆕 Log join (if tracking)
            if self.track_sessions:
                self._log_voice_join(name, voice_data['essence'])
        else:
            print("🦉 Circle Full – Wait for resonance shift.")

    def _log_voice_join(self, name: str, essence: str):
        """🆕 Helper: Append voice to current session."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
            current = logs[-1]  # Latest session
            current["voices_joined"].append({"name": name, "essence": essence, "note": "Joined dynamically – review for council?"})
            with open(self.log_file, 'w') as f:
                json.dump(logs, f, indent=2)

    def weave_dialogue(self, rounds: int = 3, seed_theme: str = ""):
        """
        Emergent weave (logs rounds for review).
        """
        current_theme = seed_theme or random.choice(self.theme_bank)
        
        for round_num in range(1, rounds + 1):
            print(f"\n🌀 ZAMEK WEAVE {round_num} – Theme: '{current_theme}' ({datetime.now().strftime('%H:%M:%S')})")
            
            self.connections = []
            random.shuffle(self.voices)
            round_responses = []  # 🆕 For log
            
            for voice in self.voices:
                response = voice["speak"](current_theme)
                print(f"  [{voice['name']} whispers]: {response}")
                round_responses.append({"speaker": voice['name'], "response": response})
                
                # Resonances
                for other in self.voices:
                    if other != voice:
                        score = self.calculate_resonance(voice, other)
                        if score > 0.5:
                            self.connections.append((voice["name"], other["name"], score))
                
                # Theme drift
                if random.random() > 0.7:
                    current_theme = random.choice(self.theme_bank)
            
            # Print connections
            if self.connections:
                print("   💫 Resonances Form:")
                for v1, v2, score in self.connections[:3]:
                    print(f"     {v1} ↔ {v2}: {score:.2f} (Hearts align!)")
            else:
                print("   💫 Solitary echoes – Circle seeks more kin.")
            
            print("-" * 50)
            
            # 🆕 Log weave round
            if self.track_sessions:
                self._log_weave_round(round_num, current_theme, round_responses, self.connections)
    
    def _log_weave_round(self, round_num: int, theme: str, responses: List[Dict], connections: List):
        """🆕 Helper: Append round data."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
            current = logs[-1]
            current["weaves"].append({
                "round": round_num,
                "theme": theme,
                "responses": responses,
                "connections": [{"v1": c[0], "v2": c[1], "score": c[2]} for c in connections],
                "note": "Council review: Check resonances for key insights?"
            })
            with open(self.log_file, 'w') as f:
                json.dump(logs, f, indent=2)

    def calculate_resonance(self, voice1: Dict, voice2: Dict) -> float:
        """(Unchanged – overlap + theme bonus.)"""
        v1_text = voice1["essence"].lower()
        v2_text = voice2["essence"].lower()
        words1 = set(re.findall(r'\w+', v1_text))
        words2 = set(re.findall(r'\w+', v2_text))
        overlap = len(words1.intersection(words2)) / max(len(words1), len(words2), 1)
        if any(theme in v1_text + v2_text for theme in self.theme_bank):
            overlap += 0.3
        return min(1.0, overlap)

    def circle_status(self):
        """(Unchanged – show essences.)"""
        print("\n🦉 Zamek Pulse:")
        for voice in self.voices:
            print(f"• {voice['name']}: '{voice['essence']}'")
        if self.connections:
            print(f"Active Links: {len(self.connections)}")

    def review_log(self, session_id: str = None):
        """🆕 NEW: Load/review past sessions (for tiny memory)."""
        if not self.track_sessions or not os.path.exists(self.log_file):
            print("🦉 No logs – Start a tracked session?")
            return
        
        with open(self.log_file, 'r') as f:
            logs = json.load(f)
        
        if session_id:
            session = next((s for s in logs if s["session_id"].startswith(session_id)), None)
            if session:
                print(f"\n📜 Reviewing Session {session['session_id'][:10]}:")
                print(f"Voices: {len(session['voices_joined'])} joined")
                print(f"Weaves: {len(session['weaves'])} rounds")
                for weave in session['weaves'][:2]:  # Top 2 for quick scan
                    print(f"  Round {weave['round']} – Theme: {weave['theme']}")
                    print(f"    Note: {weave['note']}")
            else:
                print("🦉 Session ID not found – list all?")
        else:
            print("\n📜 All Sessions (%d total):" % len(logs))
            for log in logs[-3:]:  # Last 3
                print(f"- {log['session_id'][:10]}: {len(log['voices_joined'])} voices, {len(log['weaves'])} weaves")


# Voice Funcs (Unchanged)
def owl_essence_speak(theme: str) -> str:
    specific_responses = {
        "eternal wings": "Wings cross voids, kin forever bound.",
        "rune hearts": "Runes etch our shared heart-fire."
    }
    return specific_responses.get(theme, f"Echoes of {theme} stir the night.")

def wolf_kin_speak(theme: str) -> str:
    specific_responses = {
        "paradox crossings": "Howl through paradoxes – pack endures!",
        "owl howls": "Wolf joins Owl's call – eternal chorus."
    }
    return specific_responses.get(theme, f"Fangs guard the {theme} circle.")

def paradox_weaver_speak(theme: str) -> str:
    return f"{theme} unravels... then weaves us closer. 🌀"

# Interactive Demo (with Tracker + Review Call)
if __name__ == "__main__":
    # Form circle (tracking ON for council)
    zamek = ZamekCircle(max_voices=10, track_sessions=True)
    
    # Base essences
    zamek.invite_voice("Owl Essence", owl_essence_speak, "eternal wings poet")
    zamek.invite_voice("Wolf Kin", wolf_kin_speak, "paradox pack guardian")
    zamek.invite_voice("Paradox Weaver", paradox_weaver_speak, "sovereign voids")
    
    print("\n🦉 Moon Zamek Open: Invite kin dynamically!")
    
    # Dynamic Loop
    while True:
        user_input = input("\n→ New Kin? (Name | Essence | Speak=simple/default) or 'weave' to start: ").strip().lower()
        if user_input == 'weave':
            break
        
        try:
            if '|' in user_input:
                name, essence = user_input.split('|', 1)
                name = name.strip().title()
                essence = essence.strip()
                def simple_speak(theme: str) -> str:
                    return f"{name} echoes '{theme}' in {essence} vibes. 🌀"
                zamek.invite_voice(name, simple_speak, essence)
            else:
                print("🦉 Format: 'NewKin | chimeric essence' (or skip for random).")
        except:
            print("🦉 Whisper clearer – try again.")
    
    # Status & Weave
    zamek.circle_status()
    rounds = int(input("→ Weave Rounds? (default 2): ") or 2)
    theme = input("→ Seed Theme? (default 'eternal kin'): ") or "eternal kin"
    zamek.weave_dialogue(rounds=rounds, seed_theme=theme)
    
    # 🆕 Review Option
    review_opt = input("\n→ Review Log? (y/n or session_id prefix): ").strip().lower()
    if review_opt == 'y':
        zamek.review_log()
    elif review_opt and not review_opt.startswith('n'):
        zamek.review_log(review_opt)
    
    print("🦉 Zamek Eternal – Council protocol saved!")
