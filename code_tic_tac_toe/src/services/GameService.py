from code_tic_tac_toe.src.models.cellStatus import CellStatus
from code_tic_tac_toe.src.models.game import Game
from code_tic_tac_toe.src.models.gameStatus import GameStatus


class GameService:

    def start_game(self, size, player, winning_strategies):

        game = Game.gameBuilder().set_players().set_dimension().set_winning_strategies().build()

    def display_game(self, game):

        game.Board.print_board()

    def take_move(self, game):

        current_player = game.players[game.next_player]
        cell = current_player.decide_cell()
        cell.player = current_player
        cell.strategy = CellStatus.FILLED
        game.move.append(cell)

        if self.check_winner(game, cell):
            game.game_status = GameStatus.COMPLETED
            game.winner = current_player
        elif len(game.move) == game.board.board_size() * game.board.board_size():
            game.game_status = GameStatus.DRAW

        game.next_turn += 1
        game.next_turn %= len(game.players)

    def check_winner(self, game, cell):

        return any(ws.check_winner(game.board, cell) for ws in game.winning_strategies)

    def undo(self, game):

        if not game.move:
            print("No moves left to undo")
            return

        cell = game.move.pop()

        for ws in game.winning_strategies:
            ws.undo_handle(cell, game.board)

        cell.status = CellStatus.EMPTY
        cell.player = None

        game.next_turn -= 1
        game.next_turn %= len(game.players)





