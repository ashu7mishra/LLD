from DesignPatterns.FactoryDP.knite import Knite
from DesignPatterns.FactoryDP.player_factory import PlayerFactory


class KniteFactory(PlayerFactory):

    def create_player(self):
        return Knite()
