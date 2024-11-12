
class Slots:
    def __init__(self):
        self.spinning = False
        self.final_symbols = [0, 0, 0, 0, 0]
        self.final_symbols_displayed = False
        self.symbols_bool_per_spin_lst = [False, False, False, False, False]
        self.overall_stop_conditions = [550, 1050, 1500, 1800, 2000]
        self.player_won = False
        self.total_count = 0
        self.multiplier = 0

    def check_win(self, final_symbols):
        self.multiplier = 0

        # Check for 5 in a row
        if all(final_symbols[i] == final_symbols[0] for i in range(5)):
            self.multiplier = 15
            return self.multiplier

        # Check for 4 in a row
        for i in range(2):  # Check the first two positions (0 and 1)
            if all(final_symbols[i] == final_symbols[i + j] for j in range(4)):
                self.multiplier = 10
                return self.multiplier

        # Check for 3 in a row
        for i in range(3):  # Check the first three positions (0, 1, 2)
            if all(final_symbols[i] == final_symbols[i + j] for j in range(3)):
                self.multiplier = 5
                return self.multiplier
        return self.multiplier

