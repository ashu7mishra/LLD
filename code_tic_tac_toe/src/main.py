from code_tic_tac_toe.src.controllers.gameController import GameController
from code_tic_tac_toe.src.models.bot import Bot
from code_tic_tac_toe.src.models.botDifficulty import BotDifficulty
from code_tic_tac_toe.src.models.player import Player
from code_tic_tac_toe.src.models.playerType import PlayerType
from code_tic_tac_toe.src.models.symbol import Symbol

if __name__ == '__main__':

    gc = GameController()

    dimensions = 3

    players = [
        Player('Karan', 1, PlayerType.HUMAN, Symbol('X')),
        Bot('Mohit', 2, PlayerType.BOT, Symbol('Y'), BotDifficulty.EAZY),
    ]

    winning = []

    gc.start_game(dimensions, players, winning)