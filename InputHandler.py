from InputValidator import InputValidator


class InputHandler:

    @staticmethod
    def get_player_input(matrix):
        selected_indexes = []
        while len(selected_indexes) == 0:
            selected_indexes = InputValidator.validate_input(matrix)
        
        return selected_indexes
