
class Slots:
    """
    Represents a slots machine game where a user enters a bet and spins, and either wins or loses.
    
    Attributes:
        spinning (bool): Indicates if the slots are spinning or not.
        final_symbols (list): List that contains the final symbols of the spin.
        final_symbols_displayed (bool): Indicates if the final symbols are shown.
        symbols_bool_per_spin_lst (list): List of boolean values that tracks whether each individual slot has stopped 
                                        spinning.
        overall_stop_conditions (list): List of integers that represents how many frames each individual slot should 
                                        spin.
        total_count (int): Represents each frame that the slots spin.
        multiplier (int): Multiplier for the win payout based on the number of symbols matched.
        
    Methods:
        check_win: Determines the winning multiplier based on the final symbols displayed.
    
    """
    def __init__(self):
        """Initialize the Slots game with default settings."""
        self.spinning = False
        self.final_symbols = [0, 0, 0, 0, 0]
        self.final_symbols_displayed = False
        self.symbols_bool_per_spin_lst = [False, False, False, False, False]
        self.overall_stop_conditions = [550, 1050, 1500, 1800, 2000]
        self.player_won = False
        self.total_count = 0
        self.multiplier = 0

    def check_win(self, final_symbols):
        """
        Determines the winning multiplier based on the final symbols displayed.
        
        Args:
            final_symbols (list): List that contains the final symbols of the spin.
            
        Returns:
            The winning multiplier, which is 15 if there are 5 symbols in a wor, 10 if there are 4 symbols in a row, 5
            if there are 3 symbols in a row, and 0 if there is not a match of 3 or more.
            
        """
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

