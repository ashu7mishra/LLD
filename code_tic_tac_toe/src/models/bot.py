from code_tic_tac_toe.src.helper.strategy.botFactory.botFactory import BotFactory
from code_tic_tac_toe.src.models.player import Player
from code_tic_tac_toe.src.models.playerType import PlayerType


class Bot(Player):

    def __init__(self, name, id, type, symbol, difficulty):
        super().__init__(name, id, PlayerType.BOT, symbol)
        self.difficulty = difficulty
        self.stgy = BotFactory.get_bot(self.difficulty)

    def decide_cell(self, board):
        return self.stgy.decide_move(board)