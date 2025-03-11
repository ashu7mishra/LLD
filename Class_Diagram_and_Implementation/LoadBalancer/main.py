import time

from LoadBalancer.LoadBalancerSingleton.LoadBalancer import LoadBalancer
from LoadBalancer.LoadBalancingStrategy.LeastConnectionsStrategy import LeastConnectionsStrategy
from LoadBalancer.LoadBalancingStrategy.RoundRobinStrategy import RoundRobinStrategy
from LoadBalancer.request import Request
from LoadBalancer.server import Server

if __name__ == "__main__":

    # strategy = LeastConnectionsStrategy()
    strategy = RoundRobinStrategy()
    load_balancer = LoadBalancer(strategy)

    server1 = Server(1)
    server2 = Server(2)
    server3 = Server(3)

    load_balancer.add_server(server1)
    load_balancer.add_server(server2)
    load_balancer.add_server(server3)

    for i in range(5):
        request = Request(i)
        load_balancer.distribute_request(request)
        time.sleep(1)