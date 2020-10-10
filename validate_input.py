def validate_input() -> list:
    user_input = input('Please select row and column, separated by commas (,): ').split(',')
    try:
        return list(map(lambda x: (int(x) - 1), user_input))
    except:
        print('Invalid input. Please insert a valid pair of indexes')
        return []
    