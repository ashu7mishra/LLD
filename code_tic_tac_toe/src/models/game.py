from code_tic_tac_toe.src.models.board import Board
from code_tic_tac_toe.src.models.gameStatus import GameStatus


class Game:
    def __init__(self, dimention, players, winning_strategies):
        self.players = players
        self.winning_strategies = winning_strategies
        self.Board = Board(dimention)
        self.move = []
        self.next_turn = 0
        self.winner = None
        self.game_status = GameStatus.INPROGRESS