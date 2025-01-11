from code_tic_tac_toe.src.models.player import Player
from code_tic_tac_toe.src.models.playerType import PlayerType


class Bot(Player):

    def __init__(self, name, id, type, symbol, difficulty):
        super().__init__(name, id, PlayerType.BOT, symbol)
        self.difficulty = difficulty

    def decide_cell(self, board):
        pass