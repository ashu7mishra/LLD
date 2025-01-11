from code_tic_tac_toe.src.models.game import Game


class GameService:

    def start_game(self, size, player, winning_strategies):
        game = Game.gameBuilder().set_players().set_dimension().set_winning_strategies().build()

    def display_game(self, game):
        game.Board.print_board()

    def take_move(self, game):
        current_player = game.players[game.next_player]
        cell = current_player.decide_cell()
