from DesignPatterns.DecoratorDP.add_ons.pizza_addons import PizzaAddOns


class Mushroom(PizzaAddOns):

    def get_price(self):
        return self.pizza.get_price() + 20