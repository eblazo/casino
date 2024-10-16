
class Slots:
    def __init__(self):
        self.spinning = False
        self.final_symbols = []
        self.final_symbols_displayed = False
        self.win_slots = []
        self.player_won = False

    def check_win(self, final_symbols):
        winning_indices = []
        for i in range(3):  # Check for three consecutive identical symbols
            if final_symbols[i] == final_symbols[i + 1] == final_symbols[i + 2]:
                winning_indices.extend([i, i + 1, i + 2])
                return winning_indices
        return []
