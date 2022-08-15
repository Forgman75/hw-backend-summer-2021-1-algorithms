import collections
from platform import node
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)
        print(other.inbound)
        


    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__



class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = set()
        result = []

        def inner_func(node: Node) -> list[Node]:
            if node not in visited:
                result.append(node)
                visited.add(node)
                for vertex in node.outbound:
                    inner_func(vertex)
            return result
        return inner_func(self._root)

   
    def bfs(self) -> list[Node]:
        queue = []
        visited = set()

        def inner_bfs(visited: set[Node], node: Node, queue: list[Node]) -> list[Node]:
            visited.add(node)
            queue.append(node)
            result = []
            result.append(node)
            while queue:
                vert = queue.pop(0)
                for vertex in vert.outbound:
                    if vertex not in visited:
                        visited.add(vertex)
                        queue.append(vertex)
                        result.append(vertex)
            return result

        return inner_bfs(visited, self._root, queue)

        


