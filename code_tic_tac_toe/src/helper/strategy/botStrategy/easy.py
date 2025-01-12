from code_tic_tac_toe.src.helper.strategy.botStrategy.botStgy import BotStrategy
from code_tic_tac_toe.src.models.cellStatus import CellStatus


class Easy(BotStrategy):
    def decide_move(self, board):
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell
        return None