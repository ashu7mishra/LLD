from LoadBalancer.LoadBalancingStrategy.LoadBalancingStrategy import LoadBalancerStrategy


class RoundRobinStrategy(LoadBalancerStrategy):

    def __init__(self):
        self.index = 0

    def select_server(self, servers):
        server = servers[self.index % len(servers)]
        self.index += 1
        return server
