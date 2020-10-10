class InputValidator:

    @staticmethod
    def validate_input(matrix) -> list:
        user_input = input('Please select row and column, separated by commas (,): ').split(',')
        try:
            user_input = list(map(lambda x: (int(x) - 1), user_input))
            if (InputValidator.__input_indexes_are_valid(user_input) and InputValidator.__matrix_index_is_not_taken(user_input, matrix)):
                return user_input
            else:
                return []
        except:
            return []

    @staticmethod
    def __input_indexes_are_valid(user_input) -> bool:
        if len(user_input) != 2:
            return False
        elif user_input[0] > 2 or user_input[0] < 0:
            return False
        elif user_input[1] > 2 or user_input[1] < 0:
            return False
        
        return True

    @staticmethod
    def __matrix_index_is_not_taken(user_input, matrix) -> bool:
        if matrix[user_input[0]][user_input[1]] != '?':
            return False
        return True