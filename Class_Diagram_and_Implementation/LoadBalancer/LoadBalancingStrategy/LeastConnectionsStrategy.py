from LoadBalancer.LoadBalancingStrategy.LoadBalancingStrategy import LoadBalancerStrategy


class LeastConnectionsStrategy(LoadBalancerStrategy):

    def __init__(self):
        self.index = 0

    def select_server(self, servers):
        min_connections = float('inf')
        selected_server = None

        for server in servers:
            if server.active_connections < min_connections:
                min_connections = server.active_connections
                selected_server = server

        return selected_server

