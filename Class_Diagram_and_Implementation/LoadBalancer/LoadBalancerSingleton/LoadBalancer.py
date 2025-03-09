import threading


class LoadBalancer:

    _isInstance = None
    _Lock = threading.Lock()

    def __new__(cls, strategy):
        if cls._isInstance is None:
            with cls._Lock:
                if cls._isInstance is None:
                    cls._isInstance = super(LoadBalancer, cls).__new__(cls)
                    cls._isInstance.servers = []
                    cls._isInstance.strategy = strategy
        return cls._isInstance

    def add_server(self, server):
        LoadBalancer._isInstance.servers.append(server)

    def remove_server(self, server):
        LoadBalancer._isInstance.servers.remove(server)

    def distribute_request(self, request):
        if not LoadBalancer._isInstance.servers:
            print("No servers available")

        selected_server = LoadBalancer._isInstance.strategy(LoadBalancer._isInstance.servers)
        selected_server.handle_request(request)

