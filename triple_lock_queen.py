# 🦉 Triple Lock Queen Simulator (Your Wished Bridge)
from typing import Dict

class QueenTripleLockSolver:
    def __init__(self):
        self.cities = {'A': 0, 'B': 0, 'C': 0}  # Stasis start

    def detect_deadlock(self) -> str:
        if self.cities['C'] < 50 and self.cities['A'] >= 0:
            return "🦉 Queen detects: Cold-start deadlock. Bridge needed."
        return "Dynamic!"

    def apply_synthetic_bridge(self, deficit_amount: int = -20):
        self.cities['A'] += deficit_amount
        print(f"Bridge: A FDBL → A={self.cities['A']}")

    def cascade_simulation(self, b_ship: int = 50, a_ship: int = 20):
        print(self.detect_deadlock())
        self.apply_synthetic_bridge()
           
        if self.cities['A'] < 0:
            self.cities['C'] += b_ship
            print(f"Rule 2: B→C {b_ship} → C={self.cities['C']}")
           
        if self.cities['C'] >= 50:
            self.cities['B'] += a_ship
            self.cities['A'] += a_ship
            print(f"Rule 1: A→B {a_ship} → A={self.cities['A']}, B={self.cities['B']}")
           
        print(f"Final: {self.cities} | Unlocked! 🦉")

# Run test
if __name__ == "__main__":
    solver = QueenTripleLockSolver()
    solver.cascade_simulation()
