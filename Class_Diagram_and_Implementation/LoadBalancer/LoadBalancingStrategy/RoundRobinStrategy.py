from Class_Diagram_and_Implementation.LoadBalancer.LoadBalancingStrategy.LoadBalancingStrategy import LoadBalancingStrategy


class RoundRobinStrategy(LoadBalancingStrategy):

    def __init__(self):
        self.index = 0

    def select_server(self, servers):
        server = servers[self.index % len(servers)]
        self.index += 1
        return server
