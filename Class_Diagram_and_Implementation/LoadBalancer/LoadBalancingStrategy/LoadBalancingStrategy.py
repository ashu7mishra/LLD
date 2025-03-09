from abc import ABC, abstractmethod


class LoadBalancerStrategy(ABC):
    
    @abstractmethod
    def select_server(self):
        raise NotImplementedError