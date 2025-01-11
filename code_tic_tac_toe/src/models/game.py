from code_tic_tac_toe.src.models.board import Board
from code_tic_tac_toe.src.models.gameStatus import GameStatus
from code_tic_tac_toe.src.helper.gameBuilder import GameBuilder


class Game:

    def __init__(self, dimention, players, winning_strategies):
        self.players = players
        self.winning_strategies = winning_strategies
        self.Board = Board(dimention)
        self.move = []
        self.next_turn = 0
        self.winner = None
        self.game_status = GameStatus.INPROGRESS

    @staticmethod
    def gameBuilder():
        return GameBuilder()