from threading import Lock

class Server:

    def __init__(self, server_id):
        self.server_id = server_id
        self.active_connections = 0
        self.lock = Lock()

    def handle_request(self, request):
        with self.lock:
            self.active_connections += 1

        print(f"server {self.server_id} is processing request {request.request_id} ({self.active_connections} active connections)")

        with self.lock:
            self.active_connections -= 1

        print(f"server {self.server_id} has processed request {request.request_id} ({self.active_connections} active connections)")
