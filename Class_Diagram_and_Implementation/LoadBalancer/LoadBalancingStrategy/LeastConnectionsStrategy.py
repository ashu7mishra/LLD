from Class_Diagram_and_Implementation.LoadBalancer.LoadBalancingStrategy.LoadBalancingStrategy import LoadBalancingStrategy


class LeastConnectionsStrategy(LoadBalancingStrategy):

    def __init__(self):
        self.index = 0