import threading
from concurrent.futures import Executor, as_completed

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class TreeSizeCalculator:
    def __init__(self, root: Node, executor: Executor):
        self.root = root
        self.executor = executor
        self.size = 0

    def calculate_size(self):
    # Todo for leaners
        if self.root:
            self._calculate_size_recursive(self.root)

    def _calculate_size_recursive(self, node: Node):
        # Todo for leaners
        if node:
            self.size += 1
            futures = []
            if node.left:
                futures.append(self.executor.submit(self._calculate_size_recursive,node.left))
            if node.right:
                futures.append(self.executor.submit(self._calculate_size_recursive,node.right))
            for future in as_completed(futures):
                future.result()