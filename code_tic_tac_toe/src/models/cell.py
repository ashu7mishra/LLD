from code_tic_tac_toe.src.models.cellStatus import CellStatus


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.player = None
        self.status = CellStatus.EMPTY