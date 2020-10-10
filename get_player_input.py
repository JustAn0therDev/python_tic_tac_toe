from validate_input import validate_input

def get_player_input():
    selected_indexes = []
    while(len(selected_indexes) == 0):
        selected_indexes = validate_input()
    
    return selected_indexes