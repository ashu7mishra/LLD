from DesignPatterns.DecoratorDP.add_ons.cheese import Cheese
from DesignPatterns.DecoratorDP.add_ons.mushroom import Mushroom
from DesignPatterns.DecoratorDP.base_pizza import BasePizza

if __name__ == "__main__":
    pizza = BasePizza()
    cheese_pizza = Cheese(pizza)
    mushroom_pizza = Mushroom(cheese_pizza)

    print(mushroom_pizza.get_price())


    """
        input = 'base'
        add_ons = 'cheese,mushroom,paneer'
        implement builder design pattern
    """