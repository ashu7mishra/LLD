from DesignPatterns.FactoryDP.archer_factory import ArcherFactory
from DesignPatterns.FactoryDP.knite_factory import KniteFactory


def create_player(player_val):

    if player_val == "knite":
        knite = KniteFactory()
        return knite.create_player()

    if player_val == "archer":
        archer = ArcherFactory()
        return archer.create_player()




if __name__ == "__main__":
    create_player('knite').attack()
    create_player('archer').attack()