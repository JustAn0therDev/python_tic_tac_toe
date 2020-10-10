from Player import Player

class PlayerFactory:
    @staticmethod
    def create_player(symbol, nickname):
        return Player(symbol, nickname)
