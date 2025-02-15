from DesignPatterns.FactoryDP.archer import Archer
from DesignPatterns.FactoryDP.player_factory import PlayerFactory


class ArcherFactory(PlayerFactory):

    def create_player(self):
        return Archer()