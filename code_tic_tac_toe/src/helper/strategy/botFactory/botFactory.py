# add abc for this
from code_tic_tac_toe.src.helper.strategy.botFactory.factory import Factory
from code_tic_tac_toe.src.helper.strategy.botStrategy.easy import Easy
from code_tic_tac_toe.src.models.botDifficulty import BotDifficulty


class BotFactory(Factory):

    @staticmethod
    def get_bot(difficulty):
        if difficulty == BotDifficulty.EAZY:
            return Easy()
