from DesignPatterns.DecoratorDP.pizza import Pizza


class BasePizza(Pizza):

    def get_price(self):
        return 300